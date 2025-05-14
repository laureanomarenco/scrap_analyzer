from collections import Counter
import re
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
# URL de la página web de ejemplo
url = 'https://www.infobae.com/'

@csrf_exempt
def count_words():
    print('------------- INIT SCRAP AND COUNT ---------------')
    palabras_excluir = ['dejar', 'hoy','aires','buenos','mundo','entre','ya', 'día' ,'the', 'pero', 'está', 'clarín', 'fue', 'sin', 'así', 'años', 'paso', 'medio', 'arte', 'lugar', 'sus', 'tras', 'nuevo', 'desde', 'semana', 'se', 'hizo', 'hay', 'era', 'son', 'no', 'lo', 'le', 'es', 'qué', 'cómo', 'más', 'su', 'por', 'de', 'el', 'la', 'los', 'las', 'y', 'de', 'en', 'a', 'con', 'para', 'sobre', 'un', 'una', 'que', 'del', 'al']

    titulos = scrap_titles()
    for i, titulo in enumerate(titulos, 1):
        # Extraemos el texto del título y lo convertimos a minúsculas
        texto_titulo = titulo.get_text().lower()

        # Eliminamos puntuación usando una expresión regular
        texto_limpio = re.sub(r'[^\w\s]', '', texto_titulo)

        # Dividimos el título en palabras (con un espacio como delimitador)
        palabras = [palabra for palabra in texto_limpio.split() if palabra not in palabras_excluir]
                    
        # Actualizamos el contador con las palabras encontradas
        contador.update(palabras)

    # Devolver el contador ordenado de mayor a menor frecuencia
    print(contador.most_common(25))
    print('------------- FINISH SCRAP AND COUNT ---------------')
    return contador.most_common(25)

def scrap_titles(url):
    print('------------- INIT SCRAP TLTLES---------------')
    try:
        # Realizamos una solicitud GET para obtener el contenido HTML de la página
        response = requests.get(url)

        # Verificamos que la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parseamos el contenido HTML con BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Encontramos todos los elementos <h2> con la clase "post-title"
            titulos = soup.find_all(["h1", "h2"])
            # Iteramos sobre los títulos encontrados y los mostramos
            primerosTitulos = titulos[:20]
            listaDeTitulos = []
            for i, titulo in enumerate(primerosTitulos, 1):
                # Extraemos el texto del título y lo convertimos a minúsculas
                texto_titulo = titulo.get_text()
                listaDeTitulos.append(texto_titulo)
            print(f"Los titulos mas importantes del dia son {listaDeTitulos}")
            return listaDeTitulos
    except Exception as e:
        print(f"Hubo un error al intentar acceder a la página: {e}")
        return []
