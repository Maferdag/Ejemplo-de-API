# Ejemplo-de-API
# Ejemplo-de-API

Importación de librerías
import requests
Importa la librería requests, que permite hacer solicitudes HTTP, como GET o POST, a servicios web.

from dotenv import load_dotenv
Importa la función load_dotenv desde el paquete dotenv. Esta función sirve para leer variables de entorno desde un archivo .env.

import os
Importa el módulo os, que permite interactuar con el sistema operativo, por ejemplo, para leer variables de entorno.

 Carga de variables de entorno
load_dotenv()
Ejecuta la función para cargar automáticamente las variables definidas en el archivo .env al entorno del sistema, haciéndolas accesibles desde os.getenv().

 Configuración de parámetros
API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")
Lee la clave de API de Google desde las variables de entorno. Esta clave es necesaria para autenticar las peticiones a la API.

SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
Lee el ID del motor de búsqueda personalizada que has creado en Google Custom Search.

QUERY = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
Define la búsqueda a realizar: está buscando archivos .sql (copias de bases de datos) que probablemente contengan contraseñas.

LANG = "lang_es"
Establece el idioma de los resultados como español.

START_PAGE = 1
Indica que se quiere comenzar desde la primera página de resultados de búsqueda.

 Definición de URL base
BASE_URL = "https://www.googleapis.com/customsearch/v1"
Define la URL base de la API de búsqueda personalizada de Google, donde se envían las peticiones.

 Función para construir la URL
11–14.
La función build_search_url toma los parámetros de búsqueda (consulta, página, idioma, clave de API y motor de búsqueda) y construye la URL completa para hacer la solicitud HTTP. Esto incluye todos los parámetros requeridos por Google en el formato correcto.

 Función para obtener los resultados
15–22.
La función fetch_search_results hace una solicitud HTTP a la URL generada. Si la solicitud es exitosa (sin errores), convierte la respuesta JSON en un diccionario de Python. Si ocurre un error (como problemas de red o permisos), lo imprime y retorna None.

 Función para imprimir los resultados
23–32.
La función print_results recibe una lista de resultados y los imprime por pantalla:

Si la lista está vacía, dice que no hay resultados.

Si hay resultados, imprime el título, enlace y descripción de cada uno.

 Función principal
33–40.
La función main organiza todo el flujo:

Construye la URL de búsqueda.

Llama a la API para obtener datos.

Si hay resultados (items), los manda a imprimir.

 Punto de entrada del script
41–42.
Esta línea indica que, si se ejecuta el script directamente (no si se importa desde otro archivo), se debe ejecutar la función main.