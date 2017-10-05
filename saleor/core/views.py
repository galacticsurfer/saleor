from django.template.response import TemplateResponse

from ..product.utils import products_with_availability, products_for_homepage


class Message(object):
    def __init__(self, m):
        self.message = m
        self.tags = 'warning'

    def __str__(self):
        return self.message

message = Message('Please note that, Orders placed on or after 21/08/2017 will be processed only after 28/08/2017.')


data = {
    "data": [
        {
            "created_time": "2017-09-29T19:35:24+0000",
            "reviewer": {
                "name": "Siddhant Ritwick",
                "id": "2288458067961570"
            },
            "rating": 5,
            "review_text": "Has revolutionised table tennis equipment purchase in India ! More power  to you guys"
        },
        {
            "created_time": "2017-09-28T16:07:11+0000",
            "reviewer": {
                "name": "Shahzan Magray",
                "id": "1211623995514603"
            },
            "rating": 5,
            "review_text": "Awesome service. The quality of bats is awesome"
        },
        {
            "created_time": "2017-08-18T07:14:39+0000",
            "reviewer": {
                "name": "Tulika Rajen",
                "id": "823196271043328"
            },
            "rating": 5,
            "review_text": "Matches the requirement.\nOn time delivery and very good packing.\nThe team is really helpful and they would suggest you appropriate blade, rubber which suits your nature and style of play.\nRacquets are assembled free of cost as compared to market price.\nGreat job guys \ufffd\ufffd\nThanks to Anup and Sarvotham"
        },
        {
            "created_time": "2017-08-03T09:53:16+0000",
            "reviewer": {
                "name": "Rakesh Pai",
                "id": "10153123023772803"
            },
            "rating": 5
        },
        {
            "created_time": "2017-08-03T09:49:23+0000",
            "reviewer": {
                "name": "Aks Amy Pi",
                "id": "10152526870341422"
            },
            "rating": 5
        },
        {
            "created_time": "2017-07-30T16:48:23+0000",
            "reviewer": {
                "name": "Santosh Peddi",
                "id": "1714520792094214"
            },
            "rating": 5,
            "review_text": "My ultimate table tennis product pit stop for below reasons:\nProduct suggestion based on  my game. \nAssemble is free\nProducts are of top quality \nReasonable rates compared to outlets and other sites\nFinally it's only table tennis site so easy to shop, UI is friendly and emi is added advantage.\nKudos topspin"
        },

        {
            "created_time": "2017-07-17T12:58:34+0000",
            "reviewer": {
                "name": "ABhi SHek",
                "id": "815587451832919"
            },
            "rating": 5,
            "review_text": "The bats are amazing and the quality is top notch... \nHighly recommended !!"
        },
        {
            "created_time": "2017-07-03T18:51:14+0000",
            "reviewer": {
                "name": "Debajyoti Dey Sarkar",
                "id": "1063601726986783"
            },
            "rating": 5
        },
        {
            "created_time": "2017-07-01T19:21:26+0000",
            "reviewer": {
                "name": "Adarsh Bhat",
                "id": "10210334656068719"
            },
            "rating": 5
        },
        {
            "created_time": "2017-04-05T07:15:24+0000",
            "reviewer": {
                "name": "Nithin Shetty",
                "id": "791366277550903"
            },
            "rating": 5
        },
        {
            "created_time": "2017-04-05T07:00:24+0000",
            "reviewer": {
                "name": "Kunal Mathew Verma",
                "id": "775468589164860"
            },
            "rating": 5
        },
        {
            "created_time": "2017-04-05T06:56:24+0000",
            "reviewer": {
                "name": "Abhay Pai",
                "id": "10204399706926018"
            },
            "rating": 5
        },
        {
            "created_time": "2017-04-05T06:25:01+0000",
            "reviewer": {
                "name": "Shyam Gowda",
                "id": "1234218876610294"
            },
            "rating": 4
        },
        {
            "created_time": "2017-04-04T19:13:22+0000",
            "reviewer": {
                "name": "Chaithanya Akella",
                "id": "10202308013252843"
            },
            "rating": 5
        },
        {
            "created_time": "2017-03-15T04:25:29+0000",
            "reviewer": {
                "name": "Sachin Prabhu",
                "id": "10152898097574747"
            },
            "rating": 5
        },
        {
            "created_time": "2017-03-15T04:24:26+0000",
            "reviewer": {
                "name": "Sarvotham Pai",
                "id": "10155906973459838"
            },
            "rating": 5
        },
        {
            "created_time": "2017-01-06T15:10:04+0000",
            "reviewer": {
                "name": "Manu Avadhani",
                "id": "10152876299844264"
            },
            "rating": 5
        },
        {
            "created_time": "2016-05-17T11:38:52+0000",
            "reviewer": {
                "name": "Akushay Mittal",
                "id": "1084532194895536"
            },
            "rating": 5
        }
    ],
    "paging": {
        "cursors": {
            "before": "MTAwMDAzOTIxOTYyNTU2OjU0NDkxODg3MjM1MzI1NAZDZD",
            "after": "MTAwMDAwMTYyOTc1MDk0OjU0NDkxODg3MjM1MzI1NAZDZD"
        }
    }
}


def home(request):
    products = products_for_homepage()[:16]
    products = products_with_availability(
        products, discounts=request.discounts, local_currency=request.currency)
    return TemplateResponse(
        request, 'home.html',
        {'products': products, 'parent': None, 'reviews': data['data']})
