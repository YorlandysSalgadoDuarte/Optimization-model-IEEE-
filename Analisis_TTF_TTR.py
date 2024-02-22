
from Script_Funciones import Parametros_para_MTTF_MTTR
MTTF='MTTF(horas)'
MTTR='MTTR(horas)'
Nombre_excel='Tabla4_IEEE.xlsx' # el excel debe estar dentro de la misma carpeta
import numpy as np

Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

# * Calculo de los valores aleatorios y los tiempos para TTF y TTR -----------------------------------------------------

from scipy.stats import expon
lista_paramet_dis_exp_de_MTTF, _=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)
_ , lista_paramet_dis_exp_de_MTTR=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

#! Resultados de la degradacion ===========================
degradation_U12_sin_mantenimiento=[]
degradation_U20_sin_mantenimiento=[]
degradation_U50_sin_mantenimiento=[]
degradation_U76_sin_mantenimiento=[]
degradation_U100_sin_mantenimiento=[]
degradation_U155_sin_mantenimiento=[]
degradation_U197_sin_mantenimiento=[]
degradation_U350_sin_mantenimiento=[]
degradation_U400_sin_mantenimiento=[]

#! Resultado de los tiempos de falla =======================
tiempos_de_falla_U12=[]
tiempos_de_falla_U20=[]
tiempos_de_falla_U50=[]
tiempos_de_falla_U76=[]
tiempos_de_falla_U100=[]
tiempos_de_falla_U155=[]
tiempos_de_falla_U197=[]
tiempos_de_falla_U350=[]
tiempos_de_falla_U400=[]
#! Resultado de los tiempos de reparacion =======================
tiempos_de_reparacion_U12=[]
tiempos_de_reparacion_U20=[]
tiempos_de_reparacion_U50=[]
tiempos_de_reparacion_U76=[]
tiempos_de_reparacion_U100=[]
tiempos_de_reparacion_U155=[]
tiempos_de_reparacion_U197=[]
tiempos_de_reparacion_U350=[]
tiempos_de_reparacion_U400=[]

#! CAlculo de cada Unidad:

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[0]))*1000
    tiempos_de_falla_U12.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U12)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[1]))*1000
    tiempos_de_falla_U20.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U20)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[2]))*1000
    tiempos_de_falla_U50.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U50)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[3]))*1000
    tiempos_de_falla_U76.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U76)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[4]))*1000
    tiempos_de_falla_U100.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U100)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[5]))*1000
    tiempos_de_falla_U155.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U155)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[6]))*1000
    tiempos_de_falla_U197.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U197)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[7]))*1000
    tiempos_de_falla_U350.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U350)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttf = (expon.ppf(j,lista_paramet_dis_exp_de_MTTF[0]))*1000
    tiempos_de_falla_U400.append(resultado_en_hora_ttf)
    if sum(tiempos_de_falla_U400)<=8736:
            continue
    else:break
    
#! CAlculo de cada Unidad:

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[0]))*1000
    tiempos_de_reparacion_U12.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U12)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[1]))*1000
    tiempos_de_reparacion_U20.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U20)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[2]))*1000
    tiempos_de_reparacion_U50.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U50)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[3]))*1000
    tiempos_de_reparacion_U76.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U76)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[4]))*1000
    tiempos_de_reparacion_U100.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U100)<=8736:
            continue
    else:break

datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[5]))*1000
    tiempos_de_reparacion_U155.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U155)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[6]))*1000
    tiempos_de_reparacion_U197.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U197)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[7]))*1000
    tiempos_de_reparacion_U350.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U350)<=8736:
            continue
    else:break
    
datos_uniformes = np.random.rand(10000) # Generar datos aleatorios uniformemente distribuidos entre 0 y 1
for j in datos_uniformes:
    resultado_en_hora_ttr = (expon.ppf(j,lista_paramet_dis_exp_de_MTTR[8]))*1000
    tiempos_de_reparacion_U400.append(resultado_en_hora_ttr)
    if sum(tiempos_de_reparacion_U400)<=8736:
            continue
    else:break

#TODO degradation_de las Unidades_sin_mantenimiento
#* UNIDAD 12========================================================
for i,j in zip(sorted(tiempos_de_falla_U12),sorted(tiempos_de_reparacion_U12)):
        solv=i+j
        if solv<=8760:
                degradation_U12_sin_mantenimiento.append(solv)
                comp=sum(degradation_U12_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U12_sin_mantenimiento=',degradation_U12_sin_mantenimiento)

#* UNIDAD 20========================================================
for i,j in zip(sorted(tiempos_de_falla_U20),sorted(tiempos_de_reparacion_U20)):
        solv=i+j
        if solv<=8760:
                degradation_U20_sin_mantenimiento.append(solv)
                comp=sum(degradation_U20_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U20_sin_mantenimiento=',degradation_U20_sin_mantenimiento)

#* UNIDAD 50========================================================
for i,j in zip(sorted(tiempos_de_falla_U50),sorted(tiempos_de_reparacion_U50)):
        solv=i+j
        if solv<=8760:
                degradation_U50_sin_mantenimiento.append(solv)
                comp=sum(degradation_U50_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U50_sin_mantenimiento=',degradation_U50_sin_mantenimiento)

#* UNIDAD 76========================================================
for i,j in zip(sorted(tiempos_de_falla_U76),sorted(tiempos_de_reparacion_U76)):
        solv=i+j
        if solv<=8760:
                degradation_U76_sin_mantenimiento.append(solv)
                comp=sum(degradation_U76_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U76_sin_mantenimiento=',degradation_U76_sin_mantenimiento)

#* UNIDAD 100========================================================
for i,j in zip(sorted(tiempos_de_falla_U100),sorted(tiempos_de_reparacion_U100)):
        solv=i+j
        if solv<=8760:
                degradation_U100_sin_mantenimiento.append(solv)
                comp=sum(degradation_U100_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U100_sin_mantenimiento=',degradation_U100_sin_mantenimiento)

#* UNIDAD 155========================================================
for i,j in zip(sorted(tiempos_de_falla_U155),sorted(tiempos_de_reparacion_U155)):
        solv=i+j
        if solv<=8760:
                degradation_U155_sin_mantenimiento.append(solv)
                comp=sum(degradation_U155_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U155_sin_mantenimiento=',degradation_U155_sin_mantenimiento)

#* UNIDAD 197========================================================
for i,j in zip(sorted(tiempos_de_falla_U197),sorted(tiempos_de_reparacion_U197)):
        solv=i+j
        if solv<=8760:
                degradation_U197_sin_mantenimiento.append(solv)
                comp=sum(degradation_U197_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U197_sin_mantenimiento=',degradation_U197_sin_mantenimiento)

#* UNIDAD 350========================================================
for i,j in zip(sorted(tiempos_de_falla_U350),sorted(tiempos_de_reparacion_U350)):
        solv=i+j
        if solv<=8760:
                degradation_U350_sin_mantenimiento.append(solv)
                comp=sum(degradation_U350_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U350_sin_mantenimiento=',degradation_U350_sin_mantenimiento)

#* UNIDAD 400========================================================
for i,j in zip(sorted(tiempos_de_falla_U400),sorted(tiempos_de_reparacion_U400)):
        solv=i+j
        if solv<=8760:
                degradation_U400_sin_mantenimiento.append(solv)
                comp=sum(degradation_U400_sin_mantenimiento)
                if comp>=8760:
                        break
        else:continue
print('degradation_U400_sin_mantenimiento=',degradation_U400_sin_mantenimiento)