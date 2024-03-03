 #************************************* Librerias***********************************************************************************************************************************************************************
from New_script_funciones import Parametros_para_MTTF_MTTR,crear_subplot,calculo_demanda,calulo_ttf_ttr,funcion_escalon,funcion_de_mantenimiento,AND_entre_valores,riesgo,error
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
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
pico_diario=calculo_demanda(pico_maximo,pico_maximo_por_semana_en_porciento,pico_maximo_por_dias_en_porciento,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52,pico_diario_por_horas_en_porciento_semana_18_30,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43)
# Graficar la lista
plt.plot(pico_diario)
# Mostrar el gráfico
plt.show()
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

valores_acotados_ventana_1U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_2U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_3U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_4U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_5U12 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 0, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 0, 100), 12)[:8736]
valores_acotados_ventana_1U20 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 1, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 1, 100), 20)[:8736]
valores_acotados_ventana_2U20 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 1, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 1, 100), 20)[:8736]
valores_acotados_ventana_3U20 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 1, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 1, 100), 20)[:8736]
valores_acotados_ventana_4U20 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 1, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 1, 100), 20)[:8736]
valores_acotados_ventana_1U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_2U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_3U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_4U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_5U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_6U50 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 2, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 2, 100), 50)[:8736]
valores_acotados_ventana_1U76 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 3, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 3, 100), 76)[:8736]
valores_acotados_ventana_2U76 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 3, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 3, 100), 76)[:8736]
valores_acotados_ventana_3U76 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 3, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 3, 100), 76)[:8736]
valores_acotados_ventana_4U76 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 3, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 3, 100), 76)[:8736]
valores_acotados_ventana_1U100 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 4, 100), 100)[:8736]
valores_acotados_ventana_2U100 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 4, 100), 100)[:8736]
valores_acotados_ventana_3U100 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 4, 100), 100)[:8736]
valores_acotados_ventana_1U155 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 5, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 5, 100), 155)[:8736]
valores_acotados_ventana_2U155 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 5, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 5, 100), 155)[:8736]
valores_acotados_ventana_3U155 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 5, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 5, 100), 155)[:8736]
valores_acotados_ventana_4U155 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 5, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 5, 100), 155)[:8736]
valores_acotados_ventana_1U197= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 6, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 6, 100), 197)[:8736]
valores_acotados_ventana_2U197= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 6, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 6, 100), 197)[:8736]
valores_acotados_ventana_3U197= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 6, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 6, 100), 197)[:8736]
valores_acotados_ventana_1U350= funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 7, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR, 7, 100), 350)[:8736]
valores_para_acotar_la_ventana_1U400 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 8, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,8, 400), 12)[:8736]
valores_para_acotar_la_ventana_2U400 = funcion_escalon(calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF, 8, 100), calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,8, 400), 12)[:8736]
# *************************Función para crear un subplot dado un índice****************************************
# Obtener datos para cada unidad
# Crear subgráficos para cada unidad
plt.figure(figsize=(15, 15))
crear_subplot(1, valores_acotados_ventana_1U12 ,'12')
crear_subplot(2, valores_acotados_ventana_2U12 ,'12')
crear_subplot(3, valores_acotados_ventana_3U12 ,'12')
crear_subplot(4, valores_acotados_ventana_4U12 ,'12')
crear_subplot(5, valores_acotados_ventana_5U12 ,'12')
crear_subplot(6,valores_acotados_ventana_1U20 ,'20')
crear_subplot(7,valores_acotados_ventana_2U20 ,'20')
crear_subplot(8,valores_acotados_ventana_3U20 ,'20')
crear_subplot(9,valores_acotados_ventana_4U20 ,'20')
crear_subplot(10,valores_acotados_ventana_1U50 ,'50')
crear_subplot(11,valores_acotados_ventana_2U50 ,'50')
crear_subplot(12,valores_acotados_ventana_3U50 ,'50')
crear_subplot(13,valores_acotados_ventana_4U50 ,'50')
crear_subplot(14,valores_acotados_ventana_5U50 ,'50')
crear_subplot(15,valores_acotados_ventana_6U50 ,'50')
crear_subplot(16,valores_acotados_ventana_1U76 ,'76')
crear_subplot(17,valores_acotados_ventana_2U76 ,'76')
crear_subplot(18,valores_acotados_ventana_3U76 ,'76')
crear_subplot(19,valores_acotados_ventana_4U76 ,'76')
crear_subplot(20,valores_acotados_ventana_1U100,'100')
crear_subplot(21,valores_acotados_ventana_2U100,'100')
crear_subplot(22,valores_acotados_ventana_3U100,'100')
crear_subplot(23,valores_acotados_ventana_1U155,'155')
crear_subplot(24,valores_acotados_ventana_2U155,'155')
crear_subplot(25,valores_acotados_ventana_3U155,'155')
crear_subplot(26,valores_acotados_ventana_4U155,'155')
crear_subplot(27,valores_acotados_ventana_1U197,'197')
crear_subplot(28,valores_acotados_ventana_2U197,'197')
crear_subplot(29,valores_acotados_ventana_3U197,'197')
crear_subplot(30,valores_acotados_ventana_1U350,'350')
crear_subplot(31,valores_para_acotar_la_ventana_1U400,'400')
crear_subplot(32,valores_para_acotar_la_ventana_2U400,'400')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()
# #!Tiempos de Mantenimiento-para cada maquina ---corrido---------------------------------------------------=
# ##*#########################################Semanas de Mant*dias_de_la_Semana*horas del dia**********************************************
tiempo_establ_por_IEEE_mantenimiento_1U_12 =2
tiempo_establ_por_IEEE_mantenimiento_2U_12 =2
tiempo_establ_por_IEEE_mantenimiento_3U_12 =2
tiempo_establ_por_IEEE_mantenimiento_4U_12 =2
tiempo_establ_por_IEEE_mantenimiento_5U_12 =2
tiempo_establ_por_IEEE_mantenimiento_1U_20 =2
tiempo_establ_por_IEEE_mantenimiento_2U_20 =2
tiempo_establ_por_IEEE_mantenimiento_3U_20 =2
tiempo_establ_por_IEEE_mantenimiento_4U_20 =2
tiempo_establ_por_IEEE_mantenimiento_1U_50 =2
tiempo_establ_por_IEEE_mantenimiento_2U_50 =2
tiempo_establ_por_IEEE_mantenimiento_3U_50 =2
tiempo_establ_por_IEEE_mantenimiento_4U_50 =2
tiempo_establ_por_IEEE_mantenimiento_5U_50 =2
tiempo_establ_por_IEEE_mantenimiento_6U_50 =2
tiempo_establ_por_IEEE_mantenimiento_1U_76 =3
tiempo_establ_por_IEEE_mantenimiento_2U_76 =3
tiempo_establ_por_IEEE_mantenimiento_3U_76 =3
tiempo_establ_por_IEEE_mantenimiento_4U_76 =3
tiempo_establ_por_IEEE_mantenimiento_1U_100=3
tiempo_establ_por_IEEE_mantenimiento_2U_100=3
tiempo_establ_por_IEEE_mantenimiento_3U_100=3
tiempo_establ_por_IEEE_mantenimiento_1U_155=4
tiempo_establ_por_IEEE_mantenimiento_2U_155=4
tiempo_establ_por_IEEE_mantenimiento_3U_155=4
tiempo_establ_por_IEEE_mantenimiento_4U_155=4
tiempo_establ_por_IEEE_mantenimiento_1U_197=4
tiempo_establ_por_IEEE_mantenimiento_2U_197=4
tiempo_establ_por_IEEE_mantenimiento_3U_197=4
tiempo_establ_por_IEEE_mantenimiento_1U_350=5
tiempo_establ_por_IEEE_mantenimiento_1U_400=6
tiempo_establ_por_IEEE_mantenimiento_2U_400=6

#*Valores de mantenimiento discretizados**********************************
plt.figure(figsize=(15, 15))

#***********************************VARIABLES DE MANTENIMIENTO********************************
MANT_U12_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_12,0,12)
MANT_U12_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_12,0,12)
MANT_U12_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_12,0,12)
MANT_U12_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_12,0,12)
MANT_U12_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_12,0,12)
MANT_U20_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_20,0,20)
MANT_U20_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_20,0,20)
MANT_U20_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_20,0,20)
MANT_U20_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_20,0,20)
MANT_U50_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_50,0,50)
MANT_U50_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_50,0,50)
MANT_U50_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_50,0,50)
MANT_U50_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_50,0,50)
MANT_U50_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_50,0,50)
MANT_U50_6=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_6U_50,0,50)
MANT_U76_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_76,0,76)
MANT_U76_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_76,0,76)
MANT_U76_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_76,0,76)
MANT_U76_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_76,0,76)
MANT_U100_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_100,0,100)
MANT_U100_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_100,0,100)
MANT_U100_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_100,0,100)
MANT_U155_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_155,0,155)
MANT_U155_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_155,0,155)
MANT_U155_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_155,0,155)
MANT_U155_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_155,0,155)
MANT_U197_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_197,0,197)
MANT_U197_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_197,0,197)
MANT_U197_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_197,0,197)
MANT_U350_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_350,0,350)
MANT_U400_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_400,0,400)
MANT_U400_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_400,0,400)
crear_subplot(1, MANT_U12_1,'12')
crear_subplot(2, MANT_U12_2,'12')
crear_subplot(3, MANT_U12_3,'12')
crear_subplot(4, MANT_U12_4,'12')
crear_subplot(5, MANT_U12_5,'12')
crear_subplot(6, MANT_U20_1,'20')
crear_subplot(7, MANT_U20_2,'20')
crear_subplot(8, MANT_U20_3,'20')
crear_subplot(9, MANT_U20_4,'20')
crear_subplot(10,MANT_U50_1,'50')
crear_subplot(11,MANT_U50_2,'50')
crear_subplot(12,MANT_U50_3,'50')
crear_subplot(13,MANT_U50_4,'50')
crear_subplot(14,MANT_U50_5,'50')
crear_subplot(15,MANT_U50_6,'50')
crear_subplot(16,MANT_U76_1,'76')
crear_subplot(17,MANT_U76_2,'76')
crear_subplot(18,MANT_U76_3,'76')
crear_subplot(19,MANT_U76_4,'76')
crear_subplot(20,MANT_U100_1,'100')
crear_subplot(21,MANT_U100_2,'100')
crear_subplot(22,MANT_U100_3,'100')
crear_subplot(23,MANT_U155_1,'155')
crear_subplot(24,MANT_U155_2,'155')
crear_subplot(25,MANT_U155_3,'155')
crear_subplot(26,MANT_U155_4,'155')
crear_subplot(27,MANT_U197_1,'197')
crear_subplot(28,MANT_U197_2,'197')
crear_subplot(29,MANT_U197_3,'197')
crear_subplot(30,MANT_U350_1,'350')
crear_subplot(31,MANT_U400_1,'400')
crear_subplot(32,MANT_U400_2,'400')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()

#*Desarrollo de un AND para la union de los mantenimientos y los estados de degradaion
#**********************************UNIDAD 12 *************************
AND_U12_1=AND_entre_valores(valores_acotados_ventana_2U12,MANT_U12_1,12)
crear_subplot(1, AND_U12_1,'12')

AND_U12_2=AND_entre_valores(valores_acotados_ventana_2U12,MANT_U12_2,12)
crear_subplot(2, AND_U12_2,'12')

AND_U12_3=AND_entre_valores(valores_acotados_ventana_3U12,MANT_U12_3,12)
crear_subplot(3, AND_U12_3,'12')

AND_U12_4=AND_entre_valores(valores_acotados_ventana_4U12,MANT_U12_4,12)
crear_subplot(4,AND_U12_4,'12')

AND_U12_5=AND_entre_valores(valores_acotados_ventana_5U12,MANT_U12_5,12)
crear_subplot(5, AND_U12_5,'12')

#**********************************UNIDAD 20 *************************
AND_U20_1=AND_entre_valores(valores_acotados_ventana_1U20,MANT_U20_1,20)
crear_subplot(6, AND_U20_1,'20')

AND_U20_2=AND_entre_valores(valores_acotados_ventana_2U20,MANT_U20_2,20)
crear_subplot(7, AND_U20_2,'20')

AND_U20_3=AND_entre_valores(valores_acotados_ventana_3U20,MANT_U20_3,20)
crear_subplot(8, AND_U20_3,'20')

AND_U20_4=AND_entre_valores(valores_acotados_ventana_4U20,MANT_U20_4,20)
crear_subplot(9, AND_U20_4,'20')
#**********************************UNIDAD 50 *************************
AND_U50_1=AND_entre_valores(valores_acotados_ventana_1U50,MANT_U50_1,50)
crear_subplot(10, AND_U50_1,'50')

AND_U50_2=AND_entre_valores(valores_acotados_ventana_2U50,MANT_U50_2,50)
crear_subplot(11, AND_U50_2,'50')

AND_U50_3=AND_entre_valores(valores_acotados_ventana_3U50,MANT_U50_3,50)
crear_subplot(12, AND_U50_3,'50')

AND_U50_4=AND_entre_valores(valores_acotados_ventana_4U50,MANT_U50_4,50)
crear_subplot(13,AND_U50_4,'50')

AND_U50_5=AND_entre_valores(valores_acotados_ventana_5U50,MANT_U50_5,50)
crear_subplot(14, AND_U50_5,'50')

AND_U50_6=AND_entre_valores(valores_acotados_ventana_6U50,MANT_U50_6,50)
crear_subplot(15, AND_U50_6,'50')
# Ajustar el diseño para evitar superposiciones
#**********************************UNIDAD 76 *************************
AND_U76_1=AND_entre_valores(valores_acotados_ventana_1U76,MANT_U76_1,76)
crear_subplot(16, AND_U76_1,'76')

AND_U76_2=AND_entre_valores(valores_acotados_ventana_2U76,MANT_U76_2,76)
crear_subplot(17, AND_U76_2,'76')

AND_U76_3=AND_entre_valores(valores_acotados_ventana_3U76,MANT_U76_3,76)
crear_subplot(18,AND_U76_3,'76')

AND_U76_4=AND_entre_valores(valores_acotados_ventana_4U76,MANT_U76_4,76)
crear_subplot(19, AND_U76_4,'76')
#**********************************UNIDAD 100 *************************
AND_U100_1=AND_entre_valores(valores_acotados_ventana_1U100,MANT_U100_1,100)
crear_subplot(20, AND_U100_1,'100')

AND_U100_2=AND_entre_valores(valores_acotados_ventana_2U100,MANT_U100_2,100)
crear_subplot(21, AND_U100_2,'100')

AND_U100_3=AND_entre_valores(valores_acotados_ventana_3U100,MANT_U100_3,100)
crear_subplot(22,AND_U100_3,'100')
#**********************************UNIDAD 155 *************************
AND_U155_1=AND_entre_valores(valores_acotados_ventana_1U155,MANT_U155_1,155)
crear_subplot(23,AND_U155_1,'155')

AND_U155_2=AND_entre_valores(valores_acotados_ventana_2U155,MANT_U155_2,155)
crear_subplot(24, AND_U155_2,'155')

AND_U155_3=AND_entre_valores(valores_acotados_ventana_3U155,MANT_U155_3,155)
crear_subplot(25, AND_U155_3,'155')

AND_U155_4=AND_entre_valores(valores_acotados_ventana_4U155,MANT_U155_4,155)
crear_subplot(26,AND_U155_4,'155')
#**********************************UNIDAD 197 *************************
AND_U197_1=AND_entre_valores(valores_acotados_ventana_1U197,MANT_U197_1,197)
crear_subplot(27, AND_U197_1,'197')

AND_U197_2=AND_entre_valores(valores_acotados_ventana_2U197,MANT_U197_2,197)
crear_subplot(28, AND_U197_2,'197')

AND_U197_3=AND_entre_valores(valores_acotados_ventana_3U197,MANT_U197_3,197)
crear_subplot(29,AND_U197_3,'197')
#**********************************UNIDAD 350 *************************
AND_U350_1=AND_entre_valores(valores_acotados_ventana_1U350,MANT_U350_1,350)
crear_subplot(30, AND_U350_1,'350')
#**********************************UNIDAD 400 *************************
AND_U400_1=AND_entre_valores(valores_para_acotar_la_ventana_1U400,MANT_U400_1,400)
crear_subplot(31, AND_U400_1,'400')

AND_U400_2=AND_entre_valores(valores_para_acotar_la_ventana_2U400,MANT_U400_2,400)
crear_subplot(32, AND_U400_2,'400')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()
# Mostrar todas las gráficas en una sola ventana
plt.show()

#******************************VALORES_DE_LA_DEMANDA_DISCRETIZADO***********************
resultado_suma = [a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+ab+cd+ef+gh+ij+kl for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,ab,cd,ef,gh,ij,kl in zip(AND_U12_1,AND_U12_2,AND_U12_3,AND_U12_4,AND_U12_5,
                                                                                                                                                                         AND_U20_1,AND_U20_2,AND_U20_3,AND_U20_4,
                                                                                                                                                                         AND_U50_1,AND_U50_2,AND_U50_3,AND_U50_3,AND_U50_4,AND_U50_5,AND_U50_6,
                                                                                                                                                                        AND_U76_1,AND_U76_2,AND_U76_3,AND_U76_4,
                                                                                                                                                                        AND_U100_1,AND_U100_2,AND_U100_3,
                                                                                                                                                                        AND_U155_1,AND_U155_2,AND_U155_3,AND_U155_4,
                                                                                                                                                                        AND_U197_1,AND_U197_2,AND_U197_3,
                                                                                                                                                                        AND_U350_1,
                                                                                                                                                                        AND_U400_1,AND_U400_2)]
print(resultado_suma)
# Crear un gráfico de línea
plt.plot(resultado_suma)
# Mostrar el gráfico
plt.show()

# Graficar la primera lista
plt.plot(pico_diario, label='Pico Diario')

# Graficar la segunda lista en el mismo gráfico
plt.plot(resultado_suma, label='Resultado Suma')

# Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Dos Gráficas en el Mismo Gráfico')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

#*****************************Calculo de riesgo con lo que tenenos sin implementar le modelo de optimizacion**********************************
suma_de_riesgo = riesgo(pico_diario,resultado_suma)
valor_esperado_de_riesgo=error(suma_de_riesgo,pico_diario)
print('valor_esperado_de_riesgo=',valor_esperado_de_riesgo)

