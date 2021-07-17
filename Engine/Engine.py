# coding=utf-8
import bcolors as bcolors
import sys
from Data.Api import Api
import Configuration.Config
from Configuration import Config
from Configuration import Requests
from Configuration.Display import Display
from math import *


class Engine:
    def __init__(self):
        pass

    # the user starts at the menu
    def menu(self, cursor, connection, oneProduct, allProduct):
        myDisplay = Display()
        myDisplay.displayMenu()
        x = input(bcolors.PASS)
        if x == "1":
            self.getProductByPage(1, cursor,
                                  connection, oneProduct, allProduct)
        elif x == "2":
            self.selectProduct(cursor, connection, oneProduct, allProduct)
            if x == "0":
                self.menu(cursor, connection, oneProduct, allProduct)
            else:
                text = Config.mauvaiseTouche
                print(text)
                self.menu(cursor, connection, oneProduct, allProduct)
        elif x == "3":
            self.exitClean(connection, oneProduct, allProduct)
        elif x == "7":
            self.favoriList(cursor, connection, oneProduct, allProduct)
        elif x == "9":
            self.cleanList(connection, oneProduct, allProduct)
        elif x == "5":
            self.getCategoriesByPage(1, cursor,
                                     connection, oneProduct, allProduct)
        elif x == "i":
            self.initialization(connection, oneProduct, allProduct)

        else:
            text = Config.mauvaiseTouche
            print(text)
            self.menu(cursor, connection, oneProduct, allProduct)

    # Select a detailed product by name or id
    def selectProduct(self, cursor, connection, oneProduct, allProduct):
        myDisplay = Display()
        text = Config.displaySelectProd
        print(text)
        x = input()
        if x == "1":
            myDisplay.nameProduct(cursor, connection, oneProduct, allProduct)
            self.resultProduct(cursor, connection, oneProduct, allProduct)
        elif x == "3":
            myDisplay.idProduct(cursor, connection, oneProduct, allProduct)
            self.resultProduct(cursor, connection, oneProduct, allProduct)
        elif x == "0":
            self.menu(cursor, connection, oneProduct, allProduct)
        else:
            text = Config.mauvaiseTouche
            print(text)
            self.selectProduct(cursor, connection, oneProduct, allProduct)

    # Look for a substitute of the product
    def resultProduct(self, cursor, connection, oneProduct, allProduct):
        myDisplay = Display
        answer = cursor.fetchall()
        for a in answer:
            myDisplay.displayResultProd(self=a, a=a)
            x = input(bcolors.PASS)
            if x == "1":
                substitut = (a[2],)
                request = Requests.sheachSubtitus
                cursor.execute(request, substitut)
                products = cursor.fetchall()
                # result of the best subtitu of product
                if any("a" in word for word in products):
                    for product in products:
                        if "a" in product:
                            self.substitu(product, cursor,
                                          connection, oneProduct, allProduct)
                else:
                    if any("b" in word for word in products):
                        for product in products:
                            if "b" in product:
                                self.substitu(product, cursor, connection,
                                              oneProduct, allProduct)
                    else:
                        if any("c" in word for word in products):
                            for product in products:
                                if "c" in product:
                                    self.substitu(product, cursor, connection,
                                                  oneProduct, allProduct)
                        else:
                            if any("d" in word for word in products):
                                for product in products:
                                    if "d" in product:
                                        self.substitu(product, cursor,
                                                      connection, oneProduct,
                                                      allProduct)
                            else:
                                if any("e" in word for word in products):
                                    for product in products:
                                        if "e" in product:
                                            self.substitu(product, cursor,
                                                          connection,
                                                          oneProduct,
                                                          allProduct)

            else:
                self.selectDisplay(pageNumber=0, cursor=cursor,
                                   connection=connection,
                                   oneProduct=oneProduct,
                                   allProduct=allProduct)
        else:
            text = Config.produitInnexistant
            print(text)
            self.selectProduct(cursor, connection, oneProduct, allProduct)

    # Save your favorites
    def substitu(self, product, cursor, connection, oneProduct, allProduct):
        myDisplay = Display()
        myDisplay.displaySubtitu(product)
        x = input()
        if x == "1":
            request = Requests.SaveFavorites
            val = (product[1], product[3], product[4], product[5])
            cursor.execute(request, val)
            text = Configuration.Config.saveFavory
            print(text)
            connection.commit()
            self.selectDisplay(pageNumber=0,
                               cursor=cursor, connection=connection,
                               oneProduct=oneProduct, allProduct=allProduct)
        else:
            self.selectDisplay(pageNumber=0,
                               cursor=cursor, connection=connection,
                               oneProduct=oneProduct, allProduct=allProduct)

    # Displaying products by page
    def getProductByPage(self, pageNumber, cursor, connection,
                         oneProduct, allProduct):
        # know the number of pages
        request = Requests.tcheckProducts
        cursor.execute(request)
        totalProducts = cursor.fetchall()
        processing = len(totalProducts) * 0.02
        lastPage = ceil(processing)

        # unwinding pages
        totalByPage = 50
        offset = totalByPage * (pageNumber - 1)
        minPage = 0
        request = Requests.limitOfRecords
        cursor.execute(request)
        maxPage = cursor.fetchone()[0]
        if offset < minPage:
            self.getProductByPage(lastPage,
                                  cursor, connection, oneProduct, allProduct)
        if offset > maxPage:
            self.getProductByPage(1,
                                  cursor, connection, oneProduct, allProduct)
        text = Config.displayAllProducts
        print(text)
        request = Requests.pagesOfProducts
        data = {'offset': offset}
        cursor.execute(request, data)
        myDisplay = Display()
        myDisplay.displayPageProd(cursor, offset)

        self.selectDisplay(pageNumber,
                           cursor, connection, oneProduct, allProduct)

    # Select a display (1)
    def selectDisplay(self,
                      pageNumber, cursor, connection, oneProduct, allProduct):
        myDisplay = Display()
        x = myDisplay.displayMenuProduct(pageNumber)
        if x == "0":
            self.menu(cursor, connection, oneProduct, allProduct)
        elif x == "7":
            self.getProductByPage(pageNumber - 1,
                                  cursor, connection, oneProduct, allProduct)
        elif x == "8":
            self.getProductByPage(pageNumber + 1,
                                  cursor, connection, oneProduct, allProduct)
        elif x == "2":
            self.selectProduct(cursor, connection, oneProduct, allProduct)
        elif x == "5":
            self.getCategoriesByPage(pageNumber, cursor, connection,
                                     oneProduct, allProduct)
        elif x == "3":
            self.exitClean(connection, oneProduct, allProduct)
        else:
            text = Config.mauvaiseTouche
            print(text)
            self.selectDisplay(pageNumber,
                               cursor, connection, oneProduct, allProduct)

    # Displaying categories by page
    def getCategoriesByPage(self, pageNumber, cursor, connection, oneProduct,
                            allProduct):
        # know the number of pages
        request = Requests.tcheckCategories
        cursor.execute(request)
        totalProducts = cursor.fetchall()
        processing = len(totalProducts) * 0.1
        lastPage = ceil(processing)

        # unwinding pages
        totalByPage = 10
        offset = totalByPage * (pageNumber - 1)
        minPage = 0
        request = Requests.limitOfRecords
        cursor.execute(request)
        maxPage = cursor.fetchone()[0]
        if offset < minPage:
            self.getCategoriesByPage(lastPage, cursor, connection, oneProduct,
                                     allProduct)
        if offset > maxPage:
            self.getCategoriesByPage(1, cursor, connection, oneProduct,
                                     allProduct)
        text = Config.selectCategories
        print(text)
        request = Requests.pagesOfCategories
        data = {'offset': offset}
        cursor.execute(request, data)
        products = cursor.fetchall()
        for e in products:
            print(bcolors.PASS + "[" + str(e[0]) + "] - " + e[1])
        Display.displayPageCategorie(self=allProduct,
                                     offset=offset, lastPage=lastPage)

        self.selectCategorie(pageNumber, cursor, connection, oneProduct,
                             allProduct, products, pageNumber)

    # Select a category(1)
    def selectCategorie(self, pageNumber, cursor, connection, oneProduct,
                        allProduct, products, numberOfPage):
        myDisplay = Display()

        x = myDisplay.displayMenuCategorie(numberOfPage)
        if x == "0":
            self.menu(cursor, connection, oneProduct, allProduct)
        elif x == "7":
            self.getCategoriesByPage(pageNumber - 1, cursor, connection,
                                     oneProduct, allProduct)
        elif x == "8":
            self.getCategoriesByPage(pageNumber + 1, cursor, connection,
                                     oneProduct, allProduct)
        elif x == "2":
            self.categorysProducts(pageNumber, cursor, connection, oneProduct,
                                   allProduct)
        elif x == "3":
            self.exitClean(connection, oneProduct, allProduct)

        else:
            text = Config.mauvaiseTouche
            print(text)
            self.selectCategorie(pageNumber, cursor, connection, oneProduct,
                                 allProduct, products, numberOfPage)

    # result of category
    def categorysProducts(self, pageNumber, cursor, connection, oneProduct,
                          allProduct):
        myDisplay = Display
        text = Config.selectCategoriesProd
        print(text)
        x = input(bcolors.PASS)  # enter category to view products
        text = Config.displayAllProducts2
        print(text)
        request = Requests.selectCategory
        val = ("%" + x + "%",)
        cursor.execute(request, val)
        answer = cursor.fetchall()
        val = (answer[0][1],)
        request = Requests.productsOfCategory
        cursor.execute(request, val)
        myDisplay.displayCategorysProd(self=answer, cursor=cursor)
        for a in answer:
            x = input(bcolors.PASS)
            if x == "1":  # look for a substitu
                substitut = (a[1],)
                request = Requests.sheachSubtitus
                cursor.execute(request, substitut)
                products = cursor.fetchall()
                if any("a" in word for word in products):
                    for product in products:
                        if "a" in product:
                            self.substitu(product, cursor,
                                          connection, oneProduct, allProduct)
                else:
                    if any("b" in word for word in products):
                        for product in products:
                            if "b" in product:
                                self.substitu(product, cursor, connection,
                                              oneProduct, allProduct)
                    else:
                        if any("c" in word for word in products):
                            for product in products:
                                if "c" in product:
                                    self.substitu(product, cursor, connection,
                                                  oneProduct, allProduct)
                        else:
                            if any("d" in word for word in products):
                                for product in products:
                                    if "d" in product:
                                        self.substitu(product, cursor,
                                                      connection, oneProduct,
                                                      allProduct)
                            else:
                                if any("e" in word for word in products):
                                    for product in products:
                                        if "e" in product:
                                            self.substitu(product, cursor,
                                                          connection,
                                                          oneProduct,
                                                          allProduct)
            else:
                self.getCategoriesByPage(pageNumber, cursor, connection,
                                         oneProduct, allProduct)

    # Save to user's list
    def favoriList(self, cursor, connection, oneProduct, allProduct):
        myDisplay = Display()
        request = Requests.listFavori
        cursor.execute(request)
        myDisplay.displayFavori(cursor)
        self.menu(cursor, connection, oneProduct, allProduct)

    #  empty your list
    def cleanList(self, connection, oneProduct, allProduct):
        cursor = connection.cursor()
        request = Requests.emptyList
        cursor.execute(request)
        connection.commit()
        text = Config.emptyList
        print(text)
        self.menu(cursor, connection, oneProduct, allProduct)

    def initialization(self, connection, oneProduct, allProduct):
        myApi = Api()
        cursor = connection.cursor()
        cursor.execute(Requests.cleanProducts)
        cursor.execute(Requests.cleanCategorieProd)
        myApi.dataBase()
        connection.commit()
        self.menu(cursor, connection, oneProduct, allProduct)

    # closing the program
    def exitClean(self, connection, oneProduct, allProduct):
        myDisplay = Display()
        myDisplay.goodBye()
        cursor = connection.cursor()
        cursor.execute(Requests.cleanCategorieProd)

        allProduct.append(oneProduct)
        connection.commit()

        sys.exit(1)
