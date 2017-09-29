from elasticsearch_dsl import Index


class ElasticSearch(object):
    """
    A wrapper that manages the elastic-search backend.
    """
    def rebuild_index(self, index_class, model, index_name):
        """
        utility to rebuild indexes
        :param index_class: the index class
        :param model: the model for which indexes are to be built
        :param index_name: name of index for elastic search
        :return:
        """
        my_index = Index(index_name)
        my_index.delete(ignore=404)

        my_index.doc_type(index_class)
        my_index.create()

        objects = model.objects.all()

        for obj in objects:
            obj_index = index_class.from_obj(obj)
            obj_index.save()