# coding=utf-8
from Configuration import Requests


class CategorieProd:

    def __init__(self):
        pass

    def categoriesInsert(self, cursor, connection):
        request = Requests.insertCategorieProd
        cursor.execute(request)
        connection.commit()
