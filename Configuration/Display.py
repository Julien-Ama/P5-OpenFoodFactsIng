# coding=utf-8
import bcolors as bcolors
from tabulate import tabulate
import Configuration.Config
from Configuration import Requests
from math import ceil


class Display:
    def __init__(self):
        pass

    # user view
    def displayMenu(self):
        print(bcolors.BLUE + "Veuillez inscrire le numéro "
                             "correspondant à votre recherche: \n"
              + bcolors.WARN + "1" + bcolors.BLUE +
              " - Afficher tous les produits\t\t\t\t" + bcolors.WARN + " 5"
              + bcolors.BLUE + " - Recherche des produits par catégorie\t"
              + bcolors.WARN + "i - Initialiser / "
                               "Réinitialiser tout vos produits\n"
              + bcolors.WARN + "2" + bcolors.BLUE +
              " - Sélectioner un produit détaillé\t\t\t"
              + bcolors.WARN + " 7" + bcolors.BLUE + " - Consulter votre"
              + bcolors.PASS + " ♥" + bcolors.BLUE + "liste" + bcolors.PASS +
              "♥\n" + bcolors.WARN + "3" + bcolors.BLUE +
              " - Fermer le programme\t\t\t\t\t\t"
              + bcolors.WARN + " 9 - Vider votre liste\n" + bcolors.BLUE +
              "Vous souhaitez exécuter la commande numéro :")

    # Product search by ID
    def idProduct(self, cursor):
        # Result of "nameProduct" or "idProduct:"
        print(bcolors.BLUE + "Entrez le numéro de votre produit:")

        x = input(bcolors.PASS)
        print(bcolors.BLUE + "Vous avez sélectionné le produit:",
              bcolors.PASS + "")
        request1 = ("select id, brands, categories, nutriscore_grade,"
                    " code, product_name_fr, url from products "
                    "where id like %s")
        val = ("%" + x + "%",)
        cursor.execute(request1, val)

    # Product search by name
    def nameProduct(self, cursor):
        print(bcolors.BLUE + "Entrez le nom de votre produit:")
        x = input(bcolors.PASS)
        print(bcolors.BLUE + "Vous avez sélectionné le produit:",
              bcolors.PASS + "")
        request1 = ("select id, brands, categories, nutriscore_grade,"
                    " code, product_name_fr, url from products "
                    "where product_name_fr like %s")
        val = ("%" + x + "%",)
        cursor.execute(request1, val)

    def displayResultProd(self, a):
        print("[" + str(a[0]) + "] - " + a[5] + " [" + a[2] +
              "] Nutriscore : [" + a[3] + "] code: " + a[4] + "\n" + a[6])
        print(" ")
        print(bcolors.WARN + "1" + bcolors.BLUE +
              " - Trouver un produit équivalent de meilleur qualité et "
              "les magasins qui en disposent\n"
              + bcolors.WARN + "x" + bcolors.BLUE +
              " - sélectionner n'importe quelle autre touche pour revenir "
              "en arrière")

    def displaySubtitu(self, product):
        print("[" + str(product[0]) + "] - " + product[1] +
              " [" + product[3] + "]" + bcolors.BLUE + " Magasin :"
              + bcolors.PASS + "[" + product[4] + "]" + bcolors.BLUE +
              " code :" + bcolors.PASS + "[" + product[5] + "]\n"
              + product[6])
        print("")
        print(bcolors.WARN + "Voulez-vous inscrire ce produit sur "
                             "votre liste ?")
        print(bcolors.WARN + "1" + bcolors.BLUE +
              " - Pour enregistrer ce produit sur votre liste\n"
              + bcolors.WARN + "x" + bcolors.BLUE +
              " - sélectionner n'importe quelle autre touche "
              "pour revenir en arrière")

    def displayPageProd(self, cursor, offset):
        products = cursor.fetchall()
        # to make colonized pages whose numbers follow each other vertically
        # extract from the 1st item of the list to the 41st all 10 items
        p1 = (products[0:41:10])
        # extract from the 2nd item of the list to the 42nt all 10 items
        p2 = (products[1:42:10])
        # extract from the 3rd item of the list to the 43rt all 10 items
        p3 = (products[2:43:10])
        p4 = (products[3:44:10])
        p5 = (products[4:45:10])
        p6 = (products[5:46:10])
        p7 = (products[6:47:10])
        p8 = (products[7:48:10])
        p9 = (products[8:49:10])
        p10 = (products[9:50:10])

        chapter = [[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]]
        # Configuration cleanup
        for chapt in chapter:
            cleanChapt = (tabulate(chapt))
            cleanChapt = cleanChapt.replace("(", "  ")
            cleanChapt = cleanChapt.replace(")", "  ")
            cleanChapt = cleanChapt.replace("'", bcolors.BLUE + "'"
                                            + bcolors.PASS)
            cleanChapt = cleanChapt.replace('"', " ")
            cleanChapt = cleanChapt.replace('-', bcolors.BLUE + "-"
                                            + bcolors.PASS)
            print(bcolors.PASS + cleanChapt)
        # know the number of pages
        request = Requests.tcheckProducts
        cursor.execute(request)
        totalProducts = cursor.fetchall()
        processing = len(totalProducts) * 0.02
        lastPage = ceil(processing)
        print(bcolors.WARN + "Page : [" +
              bcolors.PASS + str(int(offset / 50 + 1)) +
              bcolors.WARN + " / " + bcolors.PASS + str(lastPage) +
              bcolors.WARN + "]")
        print(" ")

        # Select a display (2)
    def displayMenuProduct(self, numberOfPage):
        print(bcolors.WARN + "0" + bcolors.BLUE +
              " - Retour au menu principal")
        print(bcolors.WARN + "2" + bcolors.BLUE +
              " - Sélectioner un produit détaillé")
        if numberOfPage == 0:
            print(bcolors.WARN + "8" + bcolors.BLUE +
                  " - Afficher tout les produits")
        if numberOfPage != 0:
            if numberOfPage != 1:
                print(bcolors.WARN + "7" + bcolors.BLUE +
                      " - Page précédente")
            print(bcolors.WARN + "8" + bcolors.BLUE + " - Page suivante")
        print(bcolors.WARN + "5" + bcolors.BLUE +
              " - Recherche des produits par catégorie")
        print(bcolors.WARN + "3" + bcolors.BLUE + " - Fermer le programme")
        return input()

    def displayPageCategorie(self, offset, lastPage):
        print(bcolors.WARN + "Page : [" +
              bcolors.PASS + str(int(offset / 10 + 1)) +
              bcolors.WARN + " / " + bcolors.PASS + str(lastPage) +
              bcolors.WARN + "]")
        print(" ")

    def displayCategorysProd(self, cursor):
        answer2 = cursor.fetchall()
        for a in answer2:
            print(str(a))
        print(" ")
        print(bcolors.WARN + "1" + bcolors.BLUE +
              " - Trouver un produit équivalent de meilleur qualité et "
              "les magasins qui en disposent\n"
              + bcolors.WARN + "x" + bcolors.BLUE +
              " - sélectionner n'importe quelle autre touche pour revenir "
              "en arrière")

    # Configuration of category search (2)
    def displayMenuCategorie(self, numberOfPage):
        print(bcolors.WARN + "0" + bcolors.BLUE +
              " - Retour au menu principal\t" + bcolors.WARN + "2" +
              bcolors.BLUE + " - Choisir une categorie par son numéro")
        if numberOfPage == 0:
            print(bcolors.WARN + "8" + bcolors.BLUE +
                  " - Afficher tout les categories")
        elif numberOfPage != 0:
            if numberOfPage != 1:
                print(bcolors.WARN + "7" + bcolors.BLUE +
                      " - Page précédente")
            print(bcolors.WARN + "8" + bcolors.BLUE + " - Page suivante")
        print(bcolors.WARN + "3" + bcolors.BLUE + " - Fermer le programme")
        return input()

    def displayFavori(self, cursor):
        myListe = cursor.fetchall()
        if len(myListe) == 0:
            print(bcolors.WARN + "Votre liste est vide")
        if len(myListe) == 1:
            print(bcolors.WARN + "Vous avez " + bcolors.PASS +
                  str(len(myListe)) + bcolors.WARN +
                  " produit sur votre liste:")
        if len(myListe) > 1:
            print(bcolors.WARN + "Vous avez " + bcolors.PASS +
                  str(len(myListe)) + bcolors.WARN +
                  " produits sur votre liste:")
        for liste in myListe:
            print(bcolors.PASS + "[" + str(liste[0]) + "] - " + liste[1] +
                  " [" + liste[2] + "]" + bcolors.BLUE + " Magasin :"
                  + bcolors.PASS + "[" + liste[3] + "]" + bcolors.BLUE +
                  " code :" + bcolors.PASS + "[" + liste[4] + "] " + liste[5])
        print("")

    def welcome(self):

        text = Configuration.Config.one
        print(text)
        text = Configuration.Config.two
        print(text)
        text = Configuration.Config.three
        print(text)
        text = Configuration.Config.four
        print(text)
        text = Configuration.Config.five
        print(text)
        text = Configuration.Config.six
        print(text)
        text = Configuration.Config.seven
        print(text)
        text = Configuration.Config.height
        print(text)
        text = Configuration.Config.nine
        print(text)
        # text = Configuration.Config.firsTime
        # print(text)

    def initAll(self, allProduct):
        if len(allProduct) == Configuration.Config.tenPercent:
            text = Configuration.Config.one
            print(text)
        if len(allProduct) == Configuration.Config.twentyPercent:
            text = Configuration.Config.two
            print(text)
        if len(allProduct) == Configuration.Config.thirtyPercent:
            text = Configuration.Config.three
            print(text)
        if len(allProduct) == Configuration.Config.fourtyPercent:
            text = Configuration.Config.four
            print(text)
        if len(allProduct) == Configuration.Config.fiftyPercent:
            text = Configuration.Config.five
            print(text)
        if len(allProduct) == Configuration.Config.sixtyPercent:
            text = Configuration.Config.six
            print(text)
        if len(allProduct) == Configuration.Config.seventyPercent:
            text = Configuration.Config.seven
            print(text)
        if len(allProduct) == Configuration.Config.eightyPercent:
            text = Configuration.Config.height
            print(text)
        if len(allProduct) == Configuration.Config.ninetyPercent:
            text = Configuration.Config.nine
            print(text)

    def goodBye(self):
        print(bcolors.WARN + "Au revoir" + bcolors.BLUE)
        print("")
        bye = [Configuration.Config.un,
               Configuration.Config.deux,
               Configuration.Config.trois,
               Configuration.Config.quatre]
        for b in bye:
            print(b)
