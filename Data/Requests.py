

# -------- REQUESTS Insert -------- #

insertProduct = "INSERT INTO product " \
                 "(brands, code, nutriscore_grade, product_name_fr, " \
                 "stores, url, categories)" \
                 "VALUES (%(brands)s,%(code)s,%(nutriscore_grade)s," \
                 "%(product_name_fr)s," \
                 "%(stores)s,%(url)s,%(categories)s)"

insertCategory = "INSERT INTO category (categories) " \
                      "SELECT DISTINCT categories FROM product " \
                      "ORDER BY categories;"

SaveFavorite = "INSERT INTO favorite " \
                "(brands, nutriscore_grade, stores, code, url) " \
                "VALUES (%s, %s, %s, %s, %s)"

# -------- REQUESTS Select -------- #

tcheckProducts = "SELECT * FROM product"

tcheckCategories = "SELECT * FROM category"

sheachSubtitus = "SELECT id, brands, categories, nutriscore_grade,"\
                 " stores, code, url from product " \
                 "WHERE categories = %s"

limitOfRecords = "SELECT count(*) FROM product"

pagesOfProducts = "SELECT id, product_name_fr FROM product " \
                  "LIMIT 50 OFFSET %(offset)s"

pagesOfCategories = "SELECT * FROM category ORDER BY categories " \
                    "LIMIT 10 OFFSET %(offset)s"

selectCategory = "SELECT * FROM category WHERE id LIKE %s"

productsOfCategory = "SELECT * FROM product " \
                     "WHERE categories LIKE %s ORDER BY nutriscore_grade "

listFavori = "SELECT * FROM favorite"


# -------- REQUESTS Truncate -------- #

emptyList = "TRUNCATE TABLE favorite"

cleanProducts = "TRUNCATE TABLE product"

cleanCategorieProd = "TRUNCATE TABLE category"
