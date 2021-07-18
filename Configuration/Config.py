# coding=utf-8
import mysql.connector
import bcolors

nbreOfProduct = 25

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


# -------- short Text -------- #

# firsTime = (bcolors.WARN +
#             "Si il s'agit de votre première utilisation, "
#             "inserez la touche: 'i'\n" + "")

displaySelectProd = (bcolors.BLUE +
                     "1 - Chercher un produit en inscrivant son nom\n"
                     "3 - Chercher un produit en incrivant son numéro\n"
                     "0 - Menu")


mauvaiseTouche = (bcolors.WARN + "Attention ! Vous avez sélectionné "
                                 "une mauvaise touche.\n""")


produitInnexistant = (bcolors.WARN + "Désolé !\n"
                                     "Ce produit n'existe pas")

displayAllProducts = (bcolors.BLUE + "voici tout les produits:")

displayAllProducts2 = (bcolors.BLUE + "Voici les produits :" +
                       bcolors.PASS + "")

selectCategories = (bcolors.BLUE +
                    "Voici les différentes catégories de produits:")

selectCategoriesProd = (bcolors.BLUE +
                        "Entrez le numéro de votre catégorie "
                        "pour y voir les produits:")

saveFavory = (bcolors.WARN +
              "Votre produit est enregistré dans votre liste\n"+"")

emptyList = (bcolors.WARN + "Votre liste est vide\n"+"")

# -------- DESIGNATE -------- #
# -------- Welcome -------- #

one = bcolors.BLUE + \
      "██    ██ █████ ██    ██████ ██████ ████████ █████    ██████ ██████" \
      "                     ░" \
      + bcolors.PASS + "░░"

two = bcolors.BLUE + \
      "██ ██ ██ ██▄▄▄ ██    ██     ██  ██ ██ ██ ██ ██▄▄▄ " \
      "     ██   ██  ██       ░" + bcolors.PASS + \
      "░░        " + bcolors.BLUE + "░" + bcolors.PASS + "░░  "

three = bcolors.BLUE + \
        "██ ██ ██ ██▀▀▀ ██    ██     ██  ██ ██ ██ ██ ██▀▀▀     " \
        " ██   ██  ██          ░" + bcolors.PASS + "░░  " \
        + bcolors.BLUE + "░" + bcolors.PASS + "░░  "

four = bcolors.BLUE + \
       "████████ █████ █████ ██████ ██████ ██    ██ █████      ██ " \
       "  ██████            ░" + bcolors.PASS + "░░   "

five = " "

six = bcolors.PASS + \
      "██████ ██████ █████ ████  ██    ██████ ██████ ██████ ███████ " \
      "   ██████ ██████ █████ ██████ █████"

seven = bcolors.WARN + \
        "██  ██ ██▄▄██ ██▄▄▄ ██ ██ ██    ██▄▄▄  ██  ██ ██  ██  ██   █ " \
        "   ██▄▄▄  ██▄▄██ ██      ██   ██▄▄▄"

height = bcolors.PASS + \
         "██  ██ ██▀▀▀▀ ██▀▀▀ ██  ████    ██▀▀▀  ██  ██ ██  ██  ██   █ " \
         "   ██▀▀▀  ██▀▀██ ██      ██   ▀▀▀██"

nine = bcolors.PASS + \
       "██████ ██     █████ ██   ███    ██     ██████ ██████ ███████ " \
       "   ██     ██  ██ █████   ██   █████"


# -------- Bye -------- #

un = bcolors.BLUE + "███████ ██████ ██████ ███████    " \
                    "██████ ██    ██ ████"
deux = bcolors.PASS + "██      ██  ██ ██  ██  ██   █     " \
                      "██▄██  ██  ██  ██▄▄"
trois = bcolors.BLUE + "██  ▀██ ██  ██ ██  ██  ██   █     " \
                       "██▀██    ██    ██▀▀"
quatre = bcolors.BLUE + "███████ ██████ ██████ ███████    " \
                        "██████    ██    ████"
