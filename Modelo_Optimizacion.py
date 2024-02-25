 #************************************* Librerias***********************************************************************************************************************************************************************
from Script_Funciones import *
from Script_Funciones import crear_subplot
from Script_Funciones import Parametros_para_MTTF_MTTR,AND_entre_valores
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
lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

print('\n#***************************Valores de ttf aleatorios **************************\n')
print('Calculo de ttf_U12',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,0,100))#U12
print('Calculo de ttf_U20',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,1,100))#U20
print('Calculo de ttf_U50',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,2,100))#U50
print('Calculo de ttf_U76',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,3,100))#U76
print('Calculo de ttf_U100',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4,100))#U100
print('Calculo de ttf_U155',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,5,100))#U155
print('Calculo de ttf_U197',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,6,100))#U197
print('Calculo de ttf_U350',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,7,100))#U350
print('Calculo de ttf_U400',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,8,100))#U400
print('\n#***************************Valores de ttr aleatorios**************************\n')
print('Calculo de ttr_U12',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,0,100))#)U12
print('Calculo de ttr_U20',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,1,100))#U20
print('Calculo de ttr_U50',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,2,100))#U50
print('Calculo de ttr_U76',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,3,100))#U76
print('Calculo de ttr_U100',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,4,100))#)U100
print('Calculo de ttr_U155',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,5,100))#)U155
print('Calculo de ttr_U197',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,6,100))#)U197
print('Calculo de ttr_U350',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,7,100))#)U350
print('Calculo de ttr_U400',calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,8,100))#U400

# *************************Ventana de valores hasta las 8736 horas****************************************
valores_acotados_ventana_U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_U20 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 1, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 1, 100), 20)[:8736]
valores_acotados_ventana_U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_U76 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 3, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 3, 100), 76)[:8736]
valores_acotados_ventana_U100 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 4, 100), 100)[:8736]
valores_acotados_ventana_U155 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 5, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 5, 100), 155)[:8736]
valores_acotados_ventana_U197= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 6, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 6, 100), 197)[:8736]
valores_acotados_ventana_U350= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 7, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 7, 100), 350)[:8736]
valores_para_acotar_la_ventana_U400 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 8, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,8, 400), 12)[:8736]
# *************************Función para crear un subplot dado un índice****************************************

# Obtener datos para cada unidad
# Crear subgráficos para cada unidad
plt.figure(figsize=(15, 15))
crear_subplot(1, valores_acotados_ventana_U12 ,'12')
crear_subplot(2,valores_acotados_ventana_U20 ,'20')
crear_subplot(3,valores_acotados_ventana_U50 ,'50')
crear_subplot(4,valores_acotados_ventana_U76 ,'76')
crear_subplot(5,valores_acotados_ventana_U100,'100')
crear_subplot(6,valores_acotados_ventana_U155,'155')
crear_subplot(7,valores_acotados_ventana_U197,'197')
crear_subplot(8,valores_acotados_ventana_U350,'350')
crear_subplot(9,valores_para_acotar_la_ventana_U400,'400')
# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()
#!Tiempos de Mantenimiento-para cada maquina ---corrido---------------------------------------------------=
##*#########################################Semanas de Mant*dias_de_la_Semana*horas del dia**********************************************
tiempo_establ_por_IEEE_mantenimiento_U_12 =2
tiempo_establ_por_IEEE_mantenimiento_U_20 =2
tiempo_establ_por_IEEE_mantenimiento_U_50 =2
tiempo_establ_por_IEEE_mantenimiento_U_76 =3
tiempo_establ_por_IEEE_mantenimiento_U_100=3
tiempo_establ_por_IEEE_mantenimiento_U_155=4
tiempo_establ_por_IEEE_mantenimiento_U_197=4
tiempo_establ_por_IEEE_mantenimiento_U_350=5
tiempo_establ_por_IEEE_mantenimiento_U_400=6

#*Valores de mantenimiento discretizados**********************************
plt.figure(figsize=(15, 15))
crear_subplot(1, funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,3,12),'12')
crear_subplot(2,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,20),'20')
crear_subplot(3,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,50),'50')
crear_subplot(4,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,76),'76')
crear_subplot(5,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,100),'100')
crear_subplot(6,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,155),'155')
crear_subplot(7,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,197),'197')
crear_subplot(8,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,5,350),'350')
crear_subplot(9,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_400,1,400),'400')
# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()

#*Desarrollo de un AND para la union de los mantenimientos y los estados de degradaion
#**********************************UNIDAD 12 *************************
AND_entre_valores(valores_acotados_ventana_U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,3,12),12)
crear_subplot(1, AND_entre_valores(valores_acotados_ventana_U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_12,3,12),12),'12')
#**********************************UNIDAD 20 *************************
AND_entre_valores(valores_acotados_ventana_U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_20,3,20),20)
crear_subplot(2, AND_entre_valores(valores_acotados_ventana_U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_20,3,20),20),'20')
#**********************************UNIDAD 50 *************************
AND_entre_valores(valores_acotados_ventana_U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_50,3,50),50)
crear_subplot(3, AND_entre_valores(valores_acotados_ventana_U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_50,3,50),50),'50')
# Ajustar el diseño para evitar superposiciones
#**********************************UNIDAD 76 *************************
AND_entre_valores(valores_acotados_ventana_U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_76,3,76),76)
crear_subplot(4, AND_entre_valores(valores_acotados_ventana_U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_76,3,76),76),'76')
#**********************************UNIDAD 100 *************************
AND_entre_valores(valores_acotados_ventana_U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_100,3,100),100)
crear_subplot(5, AND_entre_valores(valores_acotados_ventana_U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_100,3,100),100),'100')
#**********************************UNIDAD 155 *************************
AND_entre_valores(valores_acotados_ventana_U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_155,3,155),155)
crear_subplot(6, AND_entre_valores(valores_acotados_ventana_U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_155,3,155),155),'155')
#**********************************UNIDAD 197 *************************
AND_entre_valores(valores_acotados_ventana_U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_197,3,197),197)
crear_subplot(7, AND_entre_valores(valores_acotados_ventana_U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_197,3,197),197),'197')
#**********************************UNIDAD 350 *************************
AND_entre_valores(valores_acotados_ventana_U350,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_350,3,350),350)
crear_subplot(8, AND_entre_valores(valores_acotados_ventana_U350,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_350,3,350),350),'350')
#**********************************UNIDAD 400 *************************
AND_entre_valores(valores_para_acotar_la_ventana_U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_400,3,400),400)
crear_subplot(, AND_entre_valores(valores_para_acotar_la_ventana_U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_U_400,3,400),400),'400')
# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()