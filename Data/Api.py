# coding=utf-8
import mysql.connector
import requests
from databasep5.Data.Product import Product
from databasep5.Data.Category import Category
from databasep5.Configuration import Config
from databasep5.Data.Display import Display


# Step 0 data recovery
class Api:

    def __init__(self):
        pass

    def initializ(self):
        url = Config.url
        payload = Config.payload

        r = requests.get(url, payload)
        result = r.json()
        products = result["products"]
        return products

    def dataBase(self):
        # we retrieve our DATA thanks to Request and the OpenFoodFacts api
        allData = self.initializ()
        allProduct = []

        try:
            connection = Config.dataBase
            cursor = connection.cursor()
            for oneData in allData:
                # Ici on insère le code
                if "brands" in oneData.keys() and "code" in oneData.keys() and\
                   "nutriscore_grade" in oneData.keys() and\
                   "product_name_fr" in oneData.keys() and\
                   "stores" in oneData.keys() and "url" in oneData.keys() and\
                   "categories" in oneData.keys():
                    if oneData['brands'] is not None and\
                       oneData['code'] is not None and\
                       oneData['product_name_fr'] is not None and\
                       oneData['stores'] is not None and\
                       oneData['url'] is not None and\
                       oneData['nutriscore_grade'] is not None and\
                       oneData['categories'] is not None:
                        oneProduct = Product(oneData['brands'],
                                             oneData['code'],
                                             oneData['nutriscore_grade'],
                                             oneData['product_name_fr'],
                                             oneData['stores'],
                                             oneData['url'],
                                             oneData['categories'])

                        oneProduct.save(cursor)
                        allProduct.append(oneProduct)
                        connection.commit()
                        # print(cursor.rowcount, "inserted row.")
                        # print("We have", len(allProduct),
                        # "product in our allProduct")
                        myDisplay = Display()
                        myDisplay.initAll(allProduct)
                    # else:
                    #     pass
                #         print("if we are here it is because
                #         one of the values is NONE")
                #         pass
                # else:
                #     pass
                #     print("sif we are here it is because ",oneData["brands"]
                #     ," has no nutriscore")
                #     pass
            myCategories = Category()
            myCategories.categoriesInsert(cursor, connection)

        except mysql.connector.Error as error:
            print("Failed inserting allData into MySQL table {}"
                  .format(error))

        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")
