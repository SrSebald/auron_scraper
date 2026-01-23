 
import requests 
'''Definition of the url where we are going to take the data.'''
GRAPHQL_URL = ("https://www.federacionchilenadeajedrez.cl/graphql")
'''Definir los headers para pedir el formato en el que vamos a extraer la información. 
el user agent es para una identificación de que estamos haciendo
'''
HEADERS = {'Content-Type': 'application/json',
'User-Agent': 'AJEFECH-Tournament-Scraper/1.0 (contact email: werner.sebald.c@gmail.com)'}


"""Probando la Query para pedir la información a la página. las constantes son en mayusculas y las variables en minusculas."""
query = "query ($word: String!) {\n  tournaments(word: $word) {\n    id\n    title\n    city\n    start_date: startDateFormated\n    address\n    __typename\n  }\n}"

variables =  {"word": ""}

payload = {
    "query": query,
    "variables": variables
}

"Logramos hacer funcionar el payload"

print(type(payload))


"""Creando la función necesaria para que reciba la variables."""
def fetch_tournaments(word=""):
    """Me esta costando pensar en la ejecución así que lo haré paso por paso"""

    #1. darle hacer una varible con la información de word

    # Listo 
    variables = {"word": word}

    
    #2. Construir el Payload 

    #Listo
    payload = {
    "query": query,
    "variables" : variables
    }


    #3. Hacer el Post 
    response = requests.post(GRAPHQL_URL, headers=HEADERS, json=payload, timeout=10)
    #4. Validar estatus }
    if response.status_code != 200:
        raise ValueError("Networking Error")
    elif "errors" in data:
        raise ValueError("Data Error")
    elif response.status_code == 200: 
        data = response.json()

    #5 JSON

    #6 Validar errores 

    #7.Extraer los torneos 

    #8. Retornar los torneos
    return tournaments