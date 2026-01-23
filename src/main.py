from ajefech_client import fun_1

if __name__ == "__main__":




    '''Definition of the url where we are going to take the data.'''
    GRAPHQL_URL = ("https://www.federacionchilenadeajedrez.cl/graphql")

    '''Definir los headers para pedir el formato en el que vamos a extraer la información. 
    el user agent es para una identificación de que estamos haciendo
    '''
    header = {'Content-Type': 'application/json',
    'User-Agent': 'AJEFECH-Tournament-Scraper/1.0 (contact email: werner.sebald.c@gmail.com)'}


    """Probando la Query para pedir la información a la página. las constantes son en mayusculas y las variables en minusculas."""
    query = "query ($word: String!) {\n  tournaments(word: $word) {\n    id\n    title\n    city\n    start_date: startDateFormated\n    address\n    __typename\n  }\n}"

    Variables =  {"word": ""}

    payload = {
        "query": query,
        "variables": Variables
    }

    "Logramos hacer funcionar el payload"

    print(type(payload))


