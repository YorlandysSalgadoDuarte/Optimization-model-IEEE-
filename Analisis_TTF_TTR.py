import pandas as pd
import os

#! Establecer la recoleccion de datos de la tabla_4_---------------------------------------------------

# Obtiene la ruta del directorio actual donde se encuentra el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Especifica el nombre del archivo XLSX
nombre_archivo = 'Tabla4_IEEE.xlsx'

# Une la ruta del directorio actual con el nombre del archivo
ruta_archivo_xlsx = os.path.join(directorio_actual, nombre_archivo)

# Lee el archivo XLSX y carga sus datos en un DataFrame de pandas
df = pd.read_excel(nombre_archivo, engine='openpyxl')

# Ahora 'df' contiene los datos del archivo XLSX en forma de DataFrame
# Puedes imprimir el DataFrame para verificar
print(df)

#!Calcular el valor de los datos -------------------------=========================-----------------

#todo CALCULANDO PRIMERAMENTE LOS VALORES DE MTTF, la generacion de los datos tiene que ser menor que 8784
# TODOb datos que son los valores que se obtuvieron en la curva de caraga

#TODO  Extraer la columna y convertirla en una lista sobre los datos de MTTF
lista_columna_MTTF = df['MTTF(horas)'].tolist()
lista_paramet_dis_exp_de_MTTF=[]
lista_paramet_dis_exp_de_MTTR=[]
# TODO La taza de falla es igual que el medio tiempo hasta el fallo,por tanto
# TODO se puede calcular el parametro de la distribucion exponencial
for i in  lista_columna_MTTF:
    parametro_dist_exp=1/i #Parámetro Distribución Exponencial
    lista_paramet_dis_exp_de_MTTF.append(parametro_dist_exp)
# TODO Extraer la columna y convertirla en una lista sobre los datos de MTTR
# lista_columna_MTTR = df['MTTR(horas)'].tolist()
# lista_paramet_dis_exp_de_MTTR=[]
# for i in  lista_columna_MTTR:
#     parametro_dist_exp=1/i #Parámetro Distribución Exponencial
#     lista_paramet_dis_exp_de_MTTR.append(parametro_dist_exp)