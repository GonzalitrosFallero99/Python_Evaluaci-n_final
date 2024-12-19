
import requests

def obtener_pregunta():
    api = "https://opentdb.com/api.php?amount=15&difficulty=easy&type=multiple"
    mill = requests.get("https://opentdb.com/api.php?amount=15&difficulty=easy&type=multiple")
    respuesta = mill.json()
    lista = respuesta['results']
    return lista