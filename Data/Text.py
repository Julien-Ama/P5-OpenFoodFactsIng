# coding=utf-8
import bcolors

# -------- short Text -------- #

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
