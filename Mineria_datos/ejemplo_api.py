# Importamos la librería requests, que permite hacer solicitudes HTTP a páginas web o APIs
import requests

# Definimos la ciudad de la cual queremos obtener el clima
city = 'Cancún'

# Construimos la URL base del servicio wttr.in concatenando la ciudad
BASE_URL = f'https://wttr.in/{city}'

# Definimos parámetros para personalizar la respuesta:
# "m":""   → muestra la temperatura en grados Celsius (modo métrico)
# "format":3 → devuelve una salida corta en una sola línea (ejemplo: "Cancún: ☀️ +30°C")
params = {"m":"", "format":3}

# Enviamos una solicitud GET a la URL con los parámetros definidos
response = requests.get(BASE_URL, params=params)

# Mostramos el texto de la respuesta (el clima de la ciudad en formato corto)
print(response.text)
