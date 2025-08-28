# Importamos las librerías necesarias
import requests   # Para hacer solicitudes HTTP a la web
import json       # Para trabajar con datos en formato JSON

# Definimos la ciudad de la cual queremos obtener el clima
city = 'Paris'

# Construimos la URL base del servicio wttr.in
BASE_URL = f'https://wttr.in/{city}'
# (esto se traduce en: "https://wttr.in/Paris")

# Definimos los parámetros de la consulta
# "format=j1" indica que queremos la respuesta en formato JSON
PARAM = {"format": "j1"}

# Hacemos la petición GET al servidor con la URL y los parámetros definidos
response = requests.get(BASE_URL, params=PARAM)

# Convertimos la respuesta (que llega como texto) a un diccionario de Python
response_parsed = json.loads(response.text)
#print(response_parsed)

# Extraemos la sección 'current_condition' que tiene la info del clima actual
fact_weather = response_parsed['current_condition']

# Imprimimos la información en formato JSON "bonito" (con indentación)
print(json.dumps(fact_weather, indent=4))
