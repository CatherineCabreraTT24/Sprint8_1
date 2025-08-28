# Importamos las librerías necesarias
import pandas as pd                      # Para trabajar con DataFrames (tablas)
import requests                          # Para hacer solicitudes HTTP a la página
from bs4 import BeautifulSoup            # Para analizar y extraer información del HTML

# URL de la página web desde donde vamos a extraer la información
URL = 'https://tripleten-com.github.io/simple-shop_es/'

# Enviamos una solicitud GET para obtener el contenido HTML de la página
req = requests.get(URL)

# Analizamos el HTML usando BeautifulSoup con el parser 'lxml'
soup = BeautifulSoup(req.text, 'lxml')

# ------------------------------
# EXTRAEMOS LOS NOMBRES DE LOS PRODUCTOS
# ------------------------------

# Lista vacía donde guardaremos los nombres
name_products = []

# Buscamos todas las etiquetas <p> que tengan la clase correspondiente a los nombres
for row in soup.find_all(
    'p', attrs={'class': 't754__title t-name t-name_md js-product-name'}
):
    # Extraemos el texto dentro de la etiqueta y lo agregamos a la lista
    name_products.append(row.text)

# ------------------------------
# EXTRAEMOS LOS PRECIOS DE LOS PRODUCTOS
# ------------------------------

# Lista vacía donde guardaremos los precios
price = []

# Buscamos todas las etiquetas <p> que tengan la clase correspondiente a los precios
for row in soup.find_all(
    'p', attrs={'class': 't754__price-value js-product-price'}
):
    # Extraemos el texto dentro de la etiqueta y lo agregamos a la lista
    price.append(row.text)

# ------------------------------
# CREAMOS UN DATAFRAME CON PANDAS
# ------------------------------

# Inicializamos un DataFrame vacío
products_data = pd.DataFrame()

# Agregamos las columnas con los nombres y precios extraídos
products_data['name'] = name_products
products_data['price'] = price

# Mostramos las primeras 5 filas de la tabla resultante
print(products_data.head(5))
