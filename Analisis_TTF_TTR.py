import pandas as pd
import os


# Obtiene la ruta del directorio actual donde se encuentra el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Especifica el nombre del archivo XLSX
nombre_archivo = 'Tabla_4_IEEE.xlsx'

# Une la ruta del directorio actual con el nombre del archivo
ruta_archivo_xlsx = os.path.join(directorio_actual, nombre_archivo)

# Lee el archivo XLSX y carga sus datos en un DataFrame de pandas
df = pd.read_excel(nombre_archivo, engine='openpyxl')

# Ahora 'df' contiene los datos del archivo XLSX en forma de DataFrame
# Puedes imprimir el DataFrame para verificar
print(df)
