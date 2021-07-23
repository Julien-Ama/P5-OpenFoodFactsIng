# coding=utf-8
from Engine.Engine import Engine
from Data.Category import Category
from Configuration import Config


class Reception:

    def __init__(self):
        pass

    def home(self, hasData):

        allProduct = []

        connection = Config.dataBase
        cursor = connection.cursor()

        myCategories = Category()
        myCategories.categoriesInsert(cursor, connection)
        myEngine = Engine(hasData)
        myEngine.checkData(cursor, connection, allProduct)
