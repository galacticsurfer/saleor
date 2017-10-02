import json
from twisted.web.resource import Resource
from twisted.internet import defer
from twisted.python import log
from twistes.client import Elasticsearch
from twisted.web import server

import itertools

PORT = 9200
HOST = 'http://localhost'
SOME_HOSTS_CONFIG = [{
    'host': HOST,
    'port': PORT,
}]


def readBody(body, search_results):
    search_results.append(body['hits']['hits'])


def sendResponse(cb, request, search_results):
    response = []
    final_result = list(itertools.chain(*search_results))
    for result in final_result:
        result_type = result.get('_index')
        result_source = result.get('_source')
        generic_id = result_source.get('id')
        search_result = dict()
        search_result['entity_type'] = result_type
        search_result['id'] = generic_id
        search_result['name'] = result_source.get('name')
        search_result['category'] = result_source.get('category')
        search_result['price'] = result_source.get('price')
        search_result['image_url'] = result_source.get('image_url')
        hidden = result_source.get('hidden')
        if not hidden:
            response.append(search_result)
    final_response = {"products": response}
    request.write(json.dumps(final_response))
    request.finish()


class Search(object):
    def __init__(self, query):
        self.es = Elasticsearch(SOME_HOSTS_CONFIG, 30)
        self.query = dict()
        self.build_query(query)
        self.indices_map = {
            "product": "product_index",
        }

    def build_query(self, query=None):
        if query:
            self.query["from"] = 0
            self.query["size"] = 4
            self.query["query"] = dict()
            self.query["query"]["match"] = dict()
            self.query["query"]["match"]["name"] = "*%s*" % (query.lower(), )
        else:
            self.query["from"] = 0
            self.query["size"] = 4
            self.query["query"] = dict()
            self.query["query"]["match_all"] = dict()
            self.query["query"]["match_all"]["boost"] = 1.0


class SearchAPI(Resource):
    isLeaf = True
    logger = log

    def render_GET(self, request):
        request.setHeader("content-type", "application/json")
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Access-Control-Allow-Methods', 'GET')
        request.setHeader('Access-Control-Allow-Headers',
                          'x-prototype-version,x-requested-with')
        request.setHeader('Access-Control-Max-Age', 2520)

        search_results = list()
        query = request.args.get('query', None)
        if query:
            query = query[0]
        search_obj = Search(query)

        callback_refs = []
        for index, doc_type in search_obj.indices_map.items():
            sr = search_obj.es.search(index, doc_type, body=search_obj.query)
            sr.addCallback(readBody, search_results)
            callback_refs.append(sr)

        callbacks = defer.DeferredList(callback_refs)
        callbacks.addCallback(sendResponse, request, search_results)

        return server.NOT_DONE_YET

