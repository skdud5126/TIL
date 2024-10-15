from django.db import models
import requests
API_KEY = 'ttbskdud51261424002'
API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewSpecial',
            'MaxResults': '10',
            'start': '1',
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
            }
        response = requests.get(API_URL,params=params).json()
        items = response.get('item')

        for item in items:
            my_model = cls(
                            isbn = item['isbn'], 
                            author = item['author'], 
                            title = item['title'], 
                            category_name = item['categoryName'],
                            category_id = item['categoryId'],
                            price = item['priceSales'],
                            pub_date = item['pubDate'],
                            fixed_price = item['fixedPrice']
                            )
            my_model.save()