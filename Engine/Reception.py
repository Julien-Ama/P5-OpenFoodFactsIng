# coding=utf-8
from Engine.Engine import Engine
from Data.CategorieProd import CategorieProd
from Configuration import Config
from Configuration.Display import Display


class Reception:

    def __init__(self):
        pass

    def home(self, oneProduct=1):

        allProduct = []

        connection = Config.dataBase
        cursor = connection.cursor()

        allProduct.append(oneProduct)
        connection.commit()

        myDisplay = Display()
        myDisplay.welcome(allProduct)

        myCategories = CategorieProd()
        myCategories.categoriesInsert(cursor, connection)
        myEngine = Engine()
        myEngine.menu(cursor, connection, oneProduct, allProduct)
