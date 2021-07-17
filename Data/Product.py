# coding=utf-8
from Configuration import Requests


class Product:

    def __init__(self, brands, code, nutriscore_grade, product_name_fr,
                 stores, url, categories):
        self.brands = brands
        self.code = code
        self.nutriscore_grade = nutriscore_grade
        self.product_name_fr = product_name_fr
        self.stores = stores
        self.url = url
        self.categories = categories

    def save(self, cursor):

        data_product = {
            "brands": self.brands,
            "code": self.code,
            "nutriscore_grade": self.nutriscore_grade,
            "product_name_fr": self.product_name_fr,
            "stores": self.stores,
            "url": self.url,
            "categories": self.categories
        }
        my_request = Requests.insertProducts
        cursor.execute(my_request, data_product)
