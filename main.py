import requests
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Constantes de configuración
API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
QUERY = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
LANG = "lang_es"
START_PAGE = 1

# URL base de la API de Google Custom Search
BASE_URL = "https://www.googleapis.com/customsearch/v1"


def build_search_url(query, page, lang, api_key, search_engine_id):
    """
    Construye la URL para hacer la solicitud a la API de Google Custom Search.
    """
    return f"{BASE_URL}?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"


def fetch_search_results(url):
    """
    Realiza la solicitud GET a la URL proporcionada y retorna los resultados.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de error
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None


def print_results(results):
    """
    Imprime los resultados obtenidos de la API de Google Custom Search.
    """
    if not results:
        print("No se encontraron resultados.")
        return

    for item in results:
        title = item.get('title', 'Sin título')
        link = item.get('link', 'Sin enlace')
        snippet = item.get('snippet', 'Sin descripción')
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)
def main():
    """
    Función principal que orquesta la ejecución del flujo.
    """
    # Construir la URL para la API de Google Custom Search
    url = build_search_url(QUERY, START_PAGE, LANG, API_KEY, SEARCH_ENGINE_ID)

    # Obtener los resultados de la búsqueda
    data = fetch_search_results(url)

    if data:
        # Obtener los elementos de la respuesta de la API
        results = data.get('items', [])
        print_results(results)


if __name__ == "__main__":
    main()


        