# coding=utf-8
from Data import Requests


class Category:

    def __init__(self):
        pass

    def categoriesInsert(self, cursor, connection):
        request = Requests.insertCategory
        cursor.execute(request)
        connection.commit()
