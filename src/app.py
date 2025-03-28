import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import selenium
import pandas as pd

# Seleccionar el recurso a descargar
resource_url = "https://companies-market-cap-copy.vercel.app/index.html"
# Petición para descargar el fichero de Internet
response = requests.get(resource_url, time.sleep(3))

# Si la petición se ha ejecutado correctamente (código 200), entonces el contenido HTML de la página se ha podido descargar
if response:
    # Transformamos el HTML plano en un HTML real (estructurado y anidado, con forma de árbol)
    soup = BeautifulSoup(response.text, 'html')
    soup

table = soup.find("table")
data = []


for row in table.find_all("tr")[1:]:
    row_data = []  
    for cell in row.find_all("td"):
        row_data.append(cell.text.strip())  
    data.append(row_data) 

data_f = pd.DataFrame(data)
data_f[1] = data_f[1].str.replace('B','')
data_f[1] = data_f[1].str.replace('$','')
data_f
