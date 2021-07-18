

# -------- REQUESTS Insert -------- #

insertProducts = "INSERT INTO products " \
                 "(brands, code, nutriscore_grade, product_name_fr, " \
                 "stores, url, categories)" \
                 "VALUES (%(brands)s,%(code)s,%(nutriscore_grade)s," \
                 "%(product_name_fr)s," \
                 "%(stores)s,%(url)s,%(categories)s)"

insertCategorieProd = "INSERT INTO categorieprod (categories) " \
                      "SELECT DISTINCT categories FROM products " \
                      "ORDER BY categories;"

SaveFavorites = "INSERT INTO favori " \
                "(brands, nutriscore_grade, stores, code, url) " \
                "VALUES (%s, %s, %s, %s, %s)"

# -------- REQUESTS Select -------- #

tcheckProducts = "SELECT * FROM products"

tcheckCategories = "SELECT * FROM categorieprod"

sheachSubtitus = "SELECT id, brands, categories, nutriscore_grade,"\
                 " stores, code, url from products " \
                 "WHERE categories = %s"

limitOfRecords = "SELECT count(*) FROM products"

pagesOfProducts = "SELECT id, product_name_fr FROM products " \
                  "LIMIT 50 OFFSET %(offset)s"

pagesOfCategories = "SELECT * FROM categorieprod ORDER BY categories " \
                    "LIMIT 10 OFFSET %(offset)s"

selectCategory = "SELECT * FROM categorieprod WHERE id LIKE %s"

productsOfCategory = "SELECT * FROM products " \
                     "WHERE categories LIKE %s ORDER BY nutriscore_grade "

listFavori = "SELECT * FROM favori"


# -------- REQUESTS Truncate -------- #

emptyList = "TRUNCATE TABLE favori"

cleanProducts = "TRUNCATE TABLE products"

cleanCategorieProd = "TRUNCATE TABLE categorieprod"
