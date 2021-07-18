# p5-OpenFoodFactsIng

Python[3.8] - Mysql[8.0.23] - IDE:PyCharm - API:OpenFoodFacts(with Postman)

Usage :

CREATE USER 'inglese'@'localhost' IDENTIFIED BY 'passe';
GRANT ALL PRIVILEGES ON *.* TO 'inglese'@'localhost';

Please create the tables that are in: Configuration.Tables

To extract the api data, please see in Configuration.Config(Api/DB)

------------------------------------------------------------------------------

Le coeur de notre projet se trouve dans le dossier, fichier "Engine";
activé par notre fichier "Reception" et alimentée par toute les données récupérées et réparties
dans notre dossier "Data".
Notre "Engine" peut ainsi lancer son mécanisme en puisant dans notre dossier configuration 
pour y parfaire son dynamisme de requêtes et d'affichages.

Il s'agit d'une structure simple avec seulement 3 tables .

products: Table majeure où on stocke toutes les données d'api sélectionnées de OpenFoodFacts traduit en "Json".
elle a était construite en "MyISAM" pour favoriser la vitesse de lecture et donc la recherche de données.

categorieProd: Même procédé que celle de "products" mais avec uniquement les "catégories" de produits.

favori: Table vierge que l'utilisateur pourra remplir de ses produits favoris
(celle-ci puisera les données venant de la table "products")

specifications:

- [x] Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
- [x] Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
- [x] Le programme propose un substitut, sa description, un magasin ou l'acheter et un lien vers la page d'Open Food Facts concernant cet aliment.
- [x] L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données
- [x] Recherche d'aliments dans la base Open Food Facts.
- [x] L'utilisateur interagit avec le programme dans le terminal
- [x] Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question
- [x] La recherche doit s'effectuer sur une base MySql.
--------------------------------------------------------------------------------

The heart of our project is in the folder, file "Engine"; 
activated by our "Reception" file and fed by all the data recovered and distributed in our "Data" folder. 
Our "Engine" can thus launch its mechanism by drawing on our configuration folder to perfect its dynamism of requests and displays.

This is a simple structure with only 3 tables.

products: Major table where we store all the api data selected from OpenFoodFacts translated into "Json".
it was built in "MyISAM" to promote the speed of reading and therefore the search for data.

categorieProd: Same process as that of "products" but with only the "categories" of products.

favori: Blank table that the user can fill with his favorite products
(this will take the data from the "products" table)
