# coding=utf-8
import mysql.connector

nbreOfProduct = 250

ninetyPercent = round(nbreOfProduct * (0.90))
eightyPercent = round(nbreOfProduct * (0.80))
seventyPercent = round(nbreOfProduct * (0.70))
sixtyPercent = round(nbreOfProduct * (0.60))
fiftyPercent = round(nbreOfProduct * (0.50))
fourtyPercent = round(nbreOfProduct * (0.40))
thirtyPercent = round(nbreOfProduct * (0.30))
twentyPercent = round(nbreOfProduct * (0.20))
tenPercent = round(nbreOfProduct * (0.10))

# -------- Api/DB -------- #

url = 'https://world.openfoodfacts.org/cgi/search.pl?'

payload = {
            "action": "process",
            "tagtype_0": "countries",
            "json": 1,
            "search_simple": 1,
            "tag_contains_0": "contains",
            "tag_0": "france",
            "sort_by": "unique_scans_n",
            "page_size": nbreOfProduct,
            "fields": "brands,url,stores,nutriscore_grade,"
            "product_name_fr,code,categories",

        }

dataBase = mysql.connector.connect(host='localhost',
                                   database='foodfacts',
                                   user='inglese',
                                   password='passe',
                                   charset='utf8mb4')
