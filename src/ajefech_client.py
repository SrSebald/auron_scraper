 
import requests 
import unicodedata
from datetime import datetime

'''Definition of the url where we are going to take the data.'''
GRAPHQL_URL = ("https://www.federacionchilenadeajedrez.cl/graphql")
'''Definir los headers para pedir el formato en el que vamos a extraer la información. 
el user agent es para una identificación de que estamos haciendo
'''
HEADERS = {'Content-Type': 'application/json',
'User-Agent': 'AJEFECH-Tournament-Scraper/1.0 (contact email: werner.sebald.c@gmail.com)'}


"""Probando la Query para pedir la información a la página. las constantes son en mayusculas y las variables en minusculas."""
QUERY = "query ($word: String!) {\n  tournaments(word: $word) {\n    id\n    title\n    city\n    start_date: startDateFormated\n    address\n    __typename\n  }\n}"

variables =  {"word": ""}

payload = {
    "query": QUERY,
    "variables": variables
}

"Logramos hacer funcionar el payload"
#Si lo quieres probar
#print(type(payload))


"""Creando la función necesaria para que reciba la variables."""
def fetch_tournaments(word=""):
    """Me esta costando pensar en la ejecución así que lo haré paso por paso"""

    #1. darle hacer una varible con la información de word

    # Listo 
    variables = {"word": word}

    
    #2. Construir el Payload 

    #Listo
    payload = {
    "query": QUERY,
    "variables" : variables
    }


    #3. Hacer el Post 
    response = requests.post(GRAPHQL_URL, headers=HEADERS, json=payload, timeout=10)
    #4. Validar estatus 
    #6 Validar errores 
    if response.status_code != 200:
        print(response.status_code)
        print(response.text[:200])
        raise ValueError("Networking Error")
    else:
        #5 JSON
        data = response.json()
        if "errors" in data:
            raise ValueError("Data error")
        
 
    #7.Extraer los torneos 
    tournaments = data["data"]["tournaments"]


    #8. Retornar los torneos
    return tournaments

def normalize_text(s: str) -> str:
    """
    Normaliza texto para comparaciones:
    - convierte a string (por si viene None u otro tipo)
    - strip() (quita espacios extremos)
    - casefold() (mejor que lower para comparación)
    - elimina tildes/diacríticos usando unicodedata
    """
    if s is None:
        return ""

    # 1) asegurar string + limpiar bordes
    s = str(s).strip()

    # 2) minúsculas "agresivas" para comparar (mejor que lower)
    s = s.casefold()

    # 3) separar letras y diacríticos
    s = unicodedata.normalize("NFD", s)

    # 4) eliminar marcas combinantes (tildes)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")

    return s

#Vamos a crear una segunda función para normalizar los datos
#Normalización: Acción de organizariar y estructurar los datos en base a relaciones.

def normalize_tournament(t: dict):
    #1 Copiar campos base 
    base = {}

    base["id"] = t.get("id", "")

    base["title"] = t.get("title", "")

    base["city"] = t.get("city", "")

    base["start_date"] = t.get("start_date", "")

    base["address"] = t.get("address", "")

    #Limpieza de datos.

      #2 Normalizar las Mayusculas

    base["city_clean"] = base["city"].strip()

    #3 limpiar el tipo la dirección

    base["address_clean"] = base["address"].strip()


    #4 convertir la fecha
    if base["start_date"] == "":
        start_date_obj = None
    else: 
        start_date_obj = datetime.strptime(base["start_date"], "%d/%m/%Y").date()

    base["start_date_obj"] = start_date_obj
    
    #5 Calcular los booleanos

    title_n = normalize_text(base["title"])
    city_n = normalize_text(base["city_clean"])
    address_n = normalize_text(base["address_clean"])

    #Control que sea online
    ONLINE_KEYWORDS = ["lichess", "online", "chess.com"] 
    is_online = any(k in address_n for k in ONLINE_KEYWORDS)
    base["is_online"] = is_online

    #Control que sea en Santiago
    SANTIAGO_KEYWORDS =["santiago", "providencia", "nunoa", "las condes", "vitacura","la florida", "maipu", "puente alto", "san bernardo", "talagante"]
    is_santiago = any(k in  city_n for k in SANTIAGO_KEYWORDS)
    base["is_santiago"] = is_santiago

    #Control que no se haya suspendido
    SUSPEND_KEYWORDS= ["cancelado", "suspendido","suspend", "cancel"]
    is_suspend = any(k in title_n for k in SUSPEND_KEYWORDS) or any(j in city_n for j in SUSPEND_KEYWORDS )
    base["is_suspend"] = is_suspend



    #retrornar los valores normalizados.
    return  base  

