 #************************************* Librerias***********************************************************************************************************************************************************************
from New_script_funciones import Parametros_para_MTTF_MTTR,calculo_demanda,calulo_ttf_ttr,funcion_de_mantenimiento,AND_entre_valores
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np
from mealpy import FloatVar, PSO, MA, SHADE, PSS, RUN, SCA, SHIO, AOA, CEM, ASO
import time
import math
inicio=time.time()
#**********************************************************************Datos de entrada de la demanda*********************************************************************
pico_maximo = 2850 # esta dado en MW
pico_maximo_por_semana_en_porciento = [86.2,90.0,87.8,83.4,88,84.1,83.2,80.6,74,73.7,71.5,72.7,70.4,75,72.1,80,75.4,83.7,87,88,85.6,81.1,90,88.7,89.6,86.1, # de lunes a viernes
        75.5,81.6,80.1,88.0,72.2,77.6,80.0,72.9,72.6,70.5,78.0,69.5,72.4,72.4,74.3,74.4,80.0,88.1,88.5,90.9,94.0,89.0,94.2,97.0,100,95.2] # dias de la semana
pico_maximo_por_dias_en_porciento = [93,100,98,96,94,77,75]
#TODO los primeros 24 valores son para lod dias semanales y los siguientes para los fines de semana-----------------------------------------------
pico_diario_por_horas_en_porciento_semana_1_8_y_44_52 = [67,63,60,59,59,60,74,86,95,96,96,95,95,95,93,94,99,100,100,96,91,83,73,63,
                                            78,72,68,66,64,65,66,70,80,88,90,91,90,88,87,87,91,100,99,97,94,92,87,81]
pico_diario_por_horas_en_porciento_semana_18_30 = [64,60,58,56,56,58,64,76,87,95,99,100,99,100,100,97,96,96,93,92,92,93,87,72,
                                        74,70,66,65,64,62,62,66,81,86,91,93,93,92,91,91,92,94,95,95,100,93,88,80]
pico_diario_por_horas_en_porciento_semana_9_17_y_31_43 = [63,62,60,58,59,65,72,85,95,99,100,99,93,92,90,88,90,92,96,98,96,90,80,70,
                                        75,73,69,66,65,65,68,74,83,89,92,94,91,90,90,86,85,88,92,100,97,95,90,85]
#******************************************************************Calculate to Demand **************************************************************************************
pico_horario = calculo_demanda(pico_maximo,pico_maximo_por_semana_en_porciento,pico_maximo_por_dias_en_porciento,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52,pico_diario_por_horas_en_porciento_semana_18_30,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43)
#***************************************************************Mintenance and Optimization **********************************************************************************************************************************************************
def Maintenance(solution,tiempo_establ_por_IEEE_mantenimiento = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,6,6]):
#! Calculo de los valores TTR y TTF de las variables aleatorias en cada caso =================================================================================
    MTTF='MTTF(horas)'
    MTTR='MTTR(horas)'
    Nombre_excel='Table_IEEE.xlsx' # el excel debe estar dentro de la misma carpeta
    Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)
#TODO degradation_de las Unidades_sin_mantenimiento
    lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR, = Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)
    C_DEG_U12_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
    C_DEG_U12_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
    C_DEG_U12_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
    C_DEG_U12_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
    C_DEG_U12_5=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
    C_DEG_U20_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
    C_DEG_U20_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
    C_DEG_U20_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
    C_DEG_U20_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
    C_DEG_U50_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U50_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U50_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U50_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U50_5=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U50_6=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
    C_DEG_U76_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
    C_DEG_U76_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
    C_DEG_U76_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
    C_DEG_U76_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
    C_DEG_U100_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
    C_DEG_U100_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
    C_DEG_U100_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
    C_DEG_U155_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
    C_DEG_U155_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
    C_DEG_U155_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
    C_DEG_U155_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
    C_DEG_U197_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
    C_DEG_U197_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
    C_DEG_U197_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
    C_DEG_U350_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,7,50,350)[:8736]
    C_DEG_U400_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,8,50,400)[:8736]
    C_DEG_U400_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,8,50,400)[:8736]
#***********************************VARIABLES DE MANTENIMIENTO prueba con mantenimiento ********************************
    MANT_U12_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[0],0,12,solution[0])
    MANT_U12_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[1],0,12,solution[1])
    MANT_U12_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[2],0,12,solution[2])
    MANT_U12_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[3],0,12,solution[3])
    MANT_U12_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[4],0,12,solution[4])
    MANT_U20_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[5],0,20,solution[5])
    MANT_U20_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[6],0,20,solution[6])
    MANT_U20_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[7],0,20,solution[7])
    MANT_U20_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[8],0,20,solution[8])
    MANT_U50_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[9],0,50,solution[9])
    MANT_U50_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[10],0,50,solution[10])
    MANT_U50_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[11],0,50,solution[11])
    MANT_U50_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[12],0,50,solution[12])
    MANT_U50_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[13],0,50,solution[13])
    MANT_U50_6=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[14],0,50,solution[14])
    MANT_U76_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[15],0,76,solution[15])
    MANT_U76_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[16],0,76,solution[16])
    MANT_U76_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[17],0,76,solution[17])
    MANT_U76_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[18],0,76,solution[18])
    MANT_U100_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[19],0,100,solution[19])
    MANT_U100_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[20],0,100,solution[20])
    MANT_U100_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[21],0,100,solution[21])
    MANT_U155_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[22],0,155,solution[22])
    MANT_U155_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[23],0,155,solution[23])
    MANT_U155_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[24],0,155,solution[24])
    MANT_U155_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[25],0,155,solution[25])
    MANT_U197_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[26],0,197,solution[26])
    MANT_U197_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[27],0,197,solution[27])
    MANT_U197_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[28],0,197,solution[28])
    MANT_U350_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[29],0,350,solution[29])
    MANT_U400_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[30],0,400,solution[30])
    MANT_U400_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[31],0,400,solution[31])
    #*Desarrollo de un AND para la union de los mantenimientos y los estados de degradaion
#**********************************UNIDAD 12 *************************
    AND_U12_1=AND_entre_valores(C_DEG_U12_1,MANT_U12_1,12)
    AND_U12_2=AND_entre_valores(C_DEG_U12_2,MANT_U12_2,12)
    AND_U12_3=AND_entre_valores(C_DEG_U12_3,MANT_U12_3,12)
    AND_U12_4=AND_entre_valores(C_DEG_U12_4,MANT_U12_4,12)
    AND_U12_5=AND_entre_valores(C_DEG_U12_5,MANT_U12_5,12)
    #**********************************UNIDAD 20 *************************
    AND_U20_1=AND_entre_valores(C_DEG_U20_1,MANT_U20_1,20)
    AND_U20_2=AND_entre_valores(C_DEG_U20_2,MANT_U20_2,20)
    AND_U20_3=AND_entre_valores(C_DEG_U20_3,MANT_U20_3,20)
    AND_U20_4=AND_entre_valores(C_DEG_U20_4,MANT_U20_4,20)
    #**********************************UNIDAD 50 *************************
    AND_U50_1=AND_entre_valores(C_DEG_U50_1,MANT_U50_1,50)
    AND_U50_2=AND_entre_valores(C_DEG_U50_2,MANT_U50_2,50)
    AND_U50_3=AND_entre_valores(C_DEG_U50_3,MANT_U50_3,50)
    AND_U50_4=AND_entre_valores(C_DEG_U50_4,MANT_U50_4,50)
    AND_U50_5=AND_entre_valores(C_DEG_U50_5,MANT_U50_5,50)
    AND_U50_6=AND_entre_valores(C_DEG_U50_6,MANT_U50_6,50)
    #**********************************UNIDAD 76 *************************
    AND_U76_1=AND_entre_valores(C_DEG_U76_1,MANT_U76_1,76)
    AND_U76_2=AND_entre_valores(C_DEG_U76_2,MANT_U76_2,76)
    AND_U76_3=AND_entre_valores(C_DEG_U76_3,MANT_U76_3,76)
    AND_U76_4=AND_entre_valores(C_DEG_U76_4,MANT_U76_4,76)
    #**********************************UNIDAD 100 *************************
    AND_U100_1=AND_entre_valores(C_DEG_U100_1,MANT_U100_1,100)
    AND_U100_2=AND_entre_valores(C_DEG_U100_2,MANT_U100_2,100)
    AND_U100_3=AND_entre_valores(C_DEG_U100_3,MANT_U100_3,100)
    #**********************************UNIDAD 155 *************************
    AND_U155_1=AND_entre_valores(C_DEG_U155_1,MANT_U155_1,155)
    AND_U155_2=AND_entre_valores(C_DEG_U155_2,MANT_U155_2,155)
    AND_U155_3=AND_entre_valores(C_DEG_U155_3,MANT_U155_3,155)
    AND_U155_4=AND_entre_valores(C_DEG_U155_4,MANT_U155_4,155)
    #**********************************UNIDAD 197 *************************
    AND_U197_1=AND_entre_valores(C_DEG_U197_1,MANT_U197_1,197)
    AND_U197_2=AND_entre_valores(C_DEG_U197_2,MANT_U197_2,197)
    AND_U197_3=AND_entre_valores(C_DEG_U197_3,MANT_U197_3,197)
    #**********************************UNIDAD 350 *************************
    AND_U350_1=AND_entre_valores(C_DEG_U350_1,MANT_U350_1,350)
    #**********************************UNIDAD 400 *************************
    AND_U400_1=AND_entre_valores(C_DEG_U400_1,MANT_U400_1,400)
    AND_U400_2=AND_entre_valores(C_DEG_U400_2,MANT_U400_2,400)
    resultado_suma = [a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+ab+cd+ef+gh+ij+kl for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,ab,cd,ef,gh,ij,kl in zip(AND_U12_1,AND_U12_2,AND_U12_3,AND_U12_4,AND_U12_5,
                                                                                                                                                                            AND_U20_1,AND_U20_2,AND_U20_3,AND_U20_4,
                                                                                                                                                                            AND_U50_1,AND_U50_2,AND_U50_3,AND_U50_4,AND_U50_5,AND_U50_6,
                                                                                                                                                                            AND_U76_1,AND_U76_2,AND_U76_3,AND_U76_4,
                                                                                                                                                                            AND_U100_1,AND_U100_2,AND_U100_3,
                                                                                                                                                                            AND_U155_1,AND_U155_2,AND_U155_3,AND_U155_4,
                                                                                                                                                                            AND_U197_1,AND_U197_2,AND_U197_3,
                                                                                                                                                                            AND_U350_1,
                                                                                                                                                                            AND_U400_1,AND_U400_2)]
    def riesgo_Maint(demanda:list,generacion:list):
            #print(len(demanda),len(generacion))
        riesgo = []
        for i, j in zip(demanda, generacion):
            if j >= i:
                solv = 0
                riesgo.append(solv)
            if i > j:
                solv = i-j
                riesgo.append(solv)
        suma_de_riesgo = sum(riesgo)
        # print('suma_de_riesgo=',suma_de_riesgo)
        return suma_de_riesgo
    def error_Maint(suma_de_riesgo:float,pico_):
#     #?calculo de varianza en este caso para establecer el patron de parada segun montecarlos
        vector_riesgo = []
        error_Maint = []
        while  True:
            if suma_de_riesgo == 0:
                vector_riesgo.append(0)
                valor_esperado_riesgo = np.mean(vector_riesgo)
                error_Maint = None
                generacion = Simulacion_Maintenance(pico_horario, solution, tiempo_establ_por_IEEE_mantenimiento)
                suma_de_riesgo = riesgo_Maint(pico_horario,generacion)
                continue
            elif suma_de_riesgo != 0:
                vector_riesgo.append(suma_de_riesgo)
                valor_esperado_riesgo = np.mean(vector_riesgo)
                desviacion_estandar = np.std(vector_riesgo)
                error_Maint=desviacion_estandar/(valor_esperado_riesgo*math.sqrt(len(vector_riesgo)))
    #?Valor del error_Maint para el criterio de parada
                if error_Maint <= 0.05 and desviacion_estandar > 0:
                    print("el valor_esperado_riesgo del valor de riesgo es:> ", valor_esperado_riesgo)
                    print('error_Maint>', error_Maint)
                    break
                # print('error_Maint>',error_Maint)
                # print(f'el valor esperado es de {valor_esperado_riesgo} MW')
                generacion = Simulacion_Maintenance(pico_horario, solution, tiempo_establ_por_IEEE_mantenimiento)
                suma_de_riesgo = riesgo_Maint(pico_horario,generacion)
        return valor_esperado_riesgo#,error_Maint

# #**************************************************************************************************Funcion de Simulacion completada*********************************
    def Simulacion_Maintenance(pico_horario, solution, tiempo_establ_por_IEEE_mantenimiento):
        #! Calculo de los valores TTR y TTF de las variables aleatorias en cada caso =================================================================================
        MTTF='MTTF(horas)'
        MTTR='MTTR(horas)'
        Nombre_excel='Table_IEEE.xlsx' # el excel debe estar dentro de la misma carpeta
        Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)
    #TODO degradation_de las Unidades_sin_mantenimiento
        lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)
    #***************************Valores Degradacion calculados **************************\n')
        C_DEG_U12_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
        C_DEG_U12_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
        C_DEG_U12_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
        C_DEG_U12_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
        C_DEG_U12_5=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,0,50,12)[:8736]
        C_DEG_U20_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
        C_DEG_U20_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
        C_DEG_U20_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
        C_DEG_U20_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,1,50,20)[:8736]
        C_DEG_U50_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U50_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U50_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U50_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U50_5=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U50_6=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,2,50,50)[:8736]
        C_DEG_U76_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
        C_DEG_U76_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
        C_DEG_U76_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
        C_DEG_U76_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,3,50,76)[:8736]
        C_DEG_U100_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
        C_DEG_U100_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
        C_DEG_U100_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,4,50,100)[:8736]
        C_DEG_U155_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
        C_DEG_U155_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
        C_DEG_U155_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
        C_DEG_U155_4=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,5,50,155)[:8736]
        C_DEG_U197_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
        C_DEG_U197_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
        C_DEG_U197_3=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,6,50,197)[:8736]
        C_DEG_U350_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,7,50,350)[:8736]
        C_DEG_U400_1=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,8,50,400)[:8736]
        C_DEG_U400_2=calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,8,50,400)[:8736]
    # #!Tiempos de Mantenimiento-para cada maquina ---corrido---------------------------------------------------=
    #***********************************VARIABLES DE MANTENIMIENTO Optimization********************************
        MANT_U12_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[0],0,12,solution[0])
        MANT_U12_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[1],0,12,solution[1])
        MANT_U12_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[2],0,12,solution[2])
        MANT_U12_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[3],0,12,solution[3])
        MANT_U12_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[4],0,12,solution[4])
        MANT_U20_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[5],0,20,solution[5])
        MANT_U20_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[6],0,20,solution[6])
        MANT_U20_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[7],0,20,solution[7])
        MANT_U20_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[8],0,20,solution[8])
        MANT_U50_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[9],0,50,solution[9])
        MANT_U50_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[10],0,50,solution[10])
        MANT_U50_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[11],0,50,solution[11])
        MANT_U50_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[12],0,50,solution[12])
        MANT_U50_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[13],0,50,solution[13])
        MANT_U50_6=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[14],0,50,solution[14])
        MANT_U76_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[15],0,76,solution[15])
        MANT_U76_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[16],0,76,solution[16])
        MANT_U76_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[17],0,76,solution[17])
        MANT_U76_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[18],0,76,solution[18])
        MANT_U100_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[19],0,100,solution[19])
        MANT_U100_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[20],0,100,solution[20])
        MANT_U100_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[21],0,100,solution[21])
        MANT_U155_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[22],0,155,solution[22])
        MANT_U155_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[23],0,155,solution[23])
        MANT_U155_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[24],0,155,solution[24])
        MANT_U155_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[25],0,155,solution[25])
        MANT_U197_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[26],0,197,solution[26])
        MANT_U197_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[27],0,197,solution[27])
        MANT_U197_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[28],0,197,solution[28])
        MANT_U350_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[29],0,350,solution[29])
        MANT_U400_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[30],0,400,solution[30])
        MANT_U400_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento[31],0,400,solution[31])
    #*Desarrollo de un AND para la union de los mantenimientos y los estados de degradaion
    #**********************************UNIDAD 12 *************************
        AND_U12_1=AND_entre_valores(C_DEG_U12_1,MANT_U12_1,12)
        AND_U12_2=AND_entre_valores(C_DEG_U12_2,MANT_U12_2,12)
        AND_U12_3=AND_entre_valores(C_DEG_U12_3,MANT_U12_3,12)
        AND_U12_4=AND_entre_valores(C_DEG_U12_4,MANT_U12_4,12)
        AND_U12_5=AND_entre_valores(C_DEG_U12_5,MANT_U12_5,12)
    #**********************************UNIDAD 20 *************************
        AND_U20_1=AND_entre_valores(C_DEG_U20_1,MANT_U20_1,20)
        AND_U20_2=AND_entre_valores(C_DEG_U20_2,MANT_U20_2,20)
        AND_U20_3=AND_entre_valores(C_DEG_U20_3,MANT_U20_3,20)
        AND_U20_4=AND_entre_valores(C_DEG_U20_4,MANT_U20_4,20)
    #**********************************UNIDAD 50 *************************
        AND_U50_1=AND_entre_valores(C_DEG_U50_1,MANT_U50_1,50)
        AND_U50_2=AND_entre_valores(C_DEG_U50_2,MANT_U50_2,50)
        AND_U50_3=AND_entre_valores(C_DEG_U50_3,MANT_U50_3,50)
        AND_U50_4=AND_entre_valores(C_DEG_U50_4,MANT_U50_4,50)
        AND_U50_5=AND_entre_valores(C_DEG_U50_5,MANT_U50_5,50)
        AND_U50_6=AND_entre_valores(C_DEG_U50_6,MANT_U50_6,50)
    #**********************************UNIDAD 76 *************************
        AND_U76_1=AND_entre_valores(C_DEG_U76_1,MANT_U76_1,76)
        AND_U76_2=AND_entre_valores(C_DEG_U76_2,MANT_U76_2,76)
        AND_U76_3=AND_entre_valores(C_DEG_U76_3,MANT_U76_3,76)
        AND_U76_4=AND_entre_valores(C_DEG_U76_4,MANT_U76_4,76)
    #**********************************UNIDAD 100 *************************
        AND_U100_1=AND_entre_valores(C_DEG_U100_1,MANT_U100_1,100)
        AND_U100_2=AND_entre_valores(C_DEG_U100_2,MANT_U100_2,100)
        AND_U100_3=AND_entre_valores(C_DEG_U100_3,MANT_U100_3,100)
    #**********************************UNIDAD 155 *************************
        AND_U155_1=AND_entre_valores(C_DEG_U155_1,MANT_U155_1,155)
        AND_U155_2=AND_entre_valores(C_DEG_U155_2,MANT_U155_2,155)
        AND_U155_3=AND_entre_valores(C_DEG_U155_3,MANT_U155_3,155)
        AND_U155_4=AND_entre_valores(C_DEG_U155_4,MANT_U155_4,155)
    #**********************************UNIDAD 197 *************************
        AND_U197_1=AND_entre_valores(C_DEG_U197_1,MANT_U197_1,197)
        AND_U197_2=AND_entre_valores(C_DEG_U197_2,MANT_U197_2,197)
        AND_U197_3=AND_entre_valores(C_DEG_U197_3,MANT_U197_3,197)
    #**********************************UNIDAD 350 *************************
        AND_U350_1=AND_entre_valores(C_DEG_U350_1,MANT_U350_1,350)
    #**********************************UNIDAD 400 *************************
        AND_U400_1=AND_entre_valores(C_DEG_U400_1,MANT_U400_1,400)
        AND_U400_2=AND_entre_valores(C_DEG_U400_2,MANT_U400_2,400)
    #******************************VALORES_DE_LA_DEMANDA_DISCRETIZADO***********************
        resultado_suma = [a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+ab+cd+ef+gh+ij+kl for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,ab,cd,ef,gh,ij,kl in zip(AND_U12_1,AND_U12_2,AND_U12_3,AND_U12_4,AND_U12_5,
                                                                                                                                                                                AND_U20_1,AND_U20_2,AND_U20_3,AND_U20_4,
                                                                                                                                                                                AND_U50_1,AND_U50_2,AND_U50_3,AND_U50_4,AND_U50_5,AND_U50_6,
                                                                                                                                                                                AND_U76_1,AND_U76_2,AND_U76_3,AND_U76_4,
                                                                                                                                                                                AND_U100_1,AND_U100_2,AND_U100_3,
                                                                                                                                                                                AND_U155_1,AND_U155_2,AND_U155_3,AND_U155_4,
                                                                                                                                                                                AND_U197_1,AND_U197_2,AND_U197_3,
                                                                                                                                                                                AND_U350_1,
                                                                                                                                                                                AND_U400_1,AND_U400_2)]
        # # print(resultado_suma)
        # # Crear un gráfico de línea
        # plt.plot(resultado_suma)
        # # Mostrar el gráfico
        # plt.show()

        # # Graficar la primera lista
        
        # plt.plot(pico_horario, label='Pico Diario')

        # # Graficar la segunda lista en el mismo gráfico
        # plt.plot(resultado_suma, label='Resultado Suma')

        # # Añadir etiquetas y título
        # plt.xlabel('Eje X')
        # plt.ylabel('Eje Y')
        # plt.title('Dos Gráficas en el Mismo Gráfico')

        # # Mostrar leyenda
        # plt.legend()

        # # Mostrar el gráfico
        # plt.show()
        return resultado_suma

    suma_de_riesgo = riesgo_Maint(pico_horario,resultado_suma)
    valor_esperado_de_riesgo = error_Maint(suma_de_riesgo,pico_horario)
    print('valor_esperado_de_riesgo=',valor_esperado_de_riesgo)
    return valor_esperado_de_riesgo
# constraints
problem_dict = {
"bounds": FloatVar( lb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ub = [8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-2*24*7,8736-3*24*7,8736-3*24*7,8736-3*24*7,8736-3*24*7,8736-3*24*7,8736-3*24*7,8736-3*24*7,8736-4*24*7,8736-4*24*7,8736-4*24*7,8736-4*24*7,8736-4*24*7,8736-4*24*7,8736-4*24*7,8736-5*24*7,8736-6*24*7,8736-6*24*7],
                    name = "delta"),
"obj_func": Maintenance,
"minmax": "min",
}
# algorithms
# PSO
# model = PSO.OriginalPSO(epoch = 500, pop_size = 50)
# SHADE
# model = SHADE.OriginalSHADE(epoch = 500, pop_size = 50)
# model = SHADE.L_SHADE(epoch = 500, pop_size = 50)
# RUN
# model = RUN.OriginalRUN(epoch = 500, pop_size = 50)
# SCA
# model = SCA.DevSCA(epoch = 500, pop_size = 50)
# SHIO
model = SHIO.OriginalSHIO(epoch = 500, pop_size = 50)
# ASO
# model = ASO.OriginalASO(epoch = 500, pop_size = 50)
# solving the optimization
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")
print(f"Solution: {model.g_best.solution}, Fitness: {model.g_best.target.fitness}")
#TODO *********************CALCULO DEL TIEMPO DE CORRIDA**************************************
final = time.time()
print(f'tiempo de iteracion del modelo es {final - inicio}\n')