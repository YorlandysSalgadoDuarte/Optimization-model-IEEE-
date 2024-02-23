 #************************************* Librerias***********************************************************************************************************************************************************************
from Script_Funciones import *
from Script_Funciones import Parametros_para_MTTF_MTTR
import numpy as np
from scipy.stats import expon
#  #!Encontrar el pico de la demanda---------------------------------------------
#? En la tabla 5 del documento queda claro cual es el pico maximo de la demanda analizada 
pico_maximo=2850 # esta dado en MW
pico_maximo_por_semana_en_porciento=[86.2,90.0,87.8,83.4,88,84.1,83.2,80.6,74,73.7,71.5,72.7,70.4,75,72.1,80,75.4,83.7,87,88,85.6,81.1,90,88.7,89.6,86.1, # de lunes a viernes
        75.5,81.6,80.1,88.0,72.2,77.6,80.0,72.9,72.6,70.5,78.0,69.5,72.4,72.4,74.3,74.4,80.0,88.1,88.5,90.9,94.0,89.0,94.2,97.0,100,95.2] # dias de la semana
pico_maximo_por_dias_en_porciento=[93,100,98,96,94,77,75]
# en este caso particular el orden de las semanas seleccionadas en la tabla 4 me olvide de las estaciones y
# grafique en consecuencia con la continuidad de las semanas no por las estaciones
#TODO los primeros 24 valores son para lod dias semanales y los siguientes para los fines de semana-----------------------------------------------
pico_diario_por_horas_en_porciento_semana_1_8_y_44_52 =[67,63,60,59,59,60,74,86,95,96,96,95,95,95,93,94,99,100,100,96,91,83,73,63,
                                            78,72,68,66,64,65,66,70,80,88,90,91,90,88,87,87,91,100,99,97,94,92,87,81]
pico_diario_por_horas_en_porciento_semana_18_30=       [64,60,58,56,56,58,64,76,87,95,99,100,99,100,100,97,96,96,93,92,92,93,87,72,
                                        74,70,66,65,64,62,62,66,81,86,91,93,93,92,91,91,92,94,95,95,100,93,88,80]
pico_diario_por_horas_en_porciento_semana_9_17_y_31_43=[63,62,60,58,59,65,72,85,95,99,100,99,93,92,90,88,90,92,96,98,96,90,80,70,
                                        75,73,69,66,65,65,68,74,83,89,92,94,91,90,90,86,85,88,92,100,97,95,90,85]
calculo_demanda(pico_maximo,pico_maximo_por_semana_en_porciento,pico_maximo_por_dias_en_porciento,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52,pico_diario_por_horas_en_porciento_semana_18_30,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43)

#! Calculo de los valores TTR y TTF de las variables aleatorias en casda caso =================================================================================
MTTF='MTTF(horas)'
MTTR='MTTR(horas)'
Nombre_excel='Tabla4_IEEE.xlsx' # el excel debe estar dentro de la misma carpeta

Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

#TODO degradation_de las Unidades_sin_mantenimiento
lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,tiempos_de_falla_U12,tiempos_de_falla_U20,tiempos_de_falla_U50,tiempos_de_falla_U76,tiempos_de_falla_U100,tiempos_de_falla_U155,tiempos_de_falla_U197,tiempos_de_falla_U350,tiempos_de_falla_U400,tiempos_de_reparacion_U12,tiempos_de_reparacion_U20,tiempos_de_reparacion_U50,tiempos_de_reparacion_U76,tiempos_de_reparacion_U100,tiempos_de_reparacion_U155,tiempos_de_reparacion_U197,tiempos_de_reparacion_U350,tiempos_de_reparacion_U400=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

# #* UNIDAD 12=====================================
escalon_12=funcion_escalon(tiempos_de_falla_U12,tiempos_de_reparacion_U12,12)
# #* UNIDAD 20========================================================
escalon_20=funcion_escalon(tiempos_de_falla_U20,tiempos_de_reparacion_U20,20)
# #* UNIDAD 50========================================================
escalon_50=funcion_escalon(tiempos_de_falla_U50,tiempos_de_reparacion_U50,50)
# #* UNIDAD 76========================================================
escalon_76=funcion_escalon(tiempos_de_falla_U76,tiempos_de_reparacion_U76,76)
# #* UNIDAD 100========================================================
escalon_100=funcion_escalon(tiempos_de_falla_U100,tiempos_de_reparacion_U100,100)
# #* UNIDAD 155========================================================
escalon_155=funcion_escalon(tiempos_de_falla_U155,tiempos_de_reparacion_U155,155)
# #* UNIDAD 197========================================================
escalon_197=funcion_escalon(tiempos_de_falla_U197,tiempos_de_reparacion_U197,197)
# #* UNIDAD 350========================================================
escalon_350=funcion_escalon(tiempos_de_falla_U350,tiempos_de_reparacion_U350,350)
# #* UNIDAD 400========================================================
escalon_400=funcion_escalon(tiempos_de_falla_U400,tiempos_de_reparacion_U400,400)