import matplotlib.pyplot as plt
from scipy.stats import expon
import pandas as pd
import os
from Script_Funciones import *
import sympy as sp
import numpy as np
import random

def calculo_demanda(pico_maximo:int,pico_maximo_por_semana_en_porciento:list,pico_maximo_por_dias_en_porciento:int,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52:list,pico_diario_por_horas_en_porciento_semana_18_30:list,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43:list):
    #calculo a paritr de los picos maximos
    #? Variables para el calculo
    pico_maximo_por_semana=[]
    pico_maximo_por_dias=[]
    pico_diario=[]
    # Funcion para el calculo de la demadna
    for i in pico_maximo_por_semana_en_porciento:
        resultado=(pico_maximo*(i/100))
        pico_maximo_por_semana.append(resultado)

    for i in pico_maximo_por_semana :
        for j in pico_maximo_por_dias_en_porciento:
            resultado1= i *(j/100)
            pico_maximo_por_dias.append(resultado1)


    #TODo Primer grupo de valores para el calculo de la demanda--------------------------------------
    #semana_1_8_picos=pico_maximo_por_dias[:56]

    for i in pico_maximo_por_dias[0:5]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[5:7]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[7:12]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[12:14]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[14:19]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[19:21]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[21:26]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[26:28]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[28:33]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[33:35]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[35:40]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[40:42]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[42:47]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[47:49]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[49:54]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[54:56]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)

            
    #semana_9_17_pico=pico_maximo_por_dias[56:119]#----------------------------------------------------------------------
    for i in pico_maximo_por_dias[56:61]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[61:63]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[63:68]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[68:70]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[70:75]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[75:77]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[77:82]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[82:84]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[84:89]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[89:91]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[91:96]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[96:98]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[98:103]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[103:105]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[105:110]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[110:112]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[112:117]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[117:119]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)

    #semana_18_30_pico=pico_maximo_por_dias[119:210]#----------------------------------------------------------------------

    for i in pico_maximo_por_dias[119:124]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[124:126]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[126:131]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[131:133]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[133:138]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[138:140]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[140:145]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[145:147]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[147:152]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[152:154]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[154:159]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[159:161]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[161:166]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[166:168]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[168:173]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[173:175]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[175:180]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[180:182]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[182:187]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[187:189]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[189:194]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[194:196]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[196:201]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[201:203]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[203:208]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[208:210]:
        for j in pico_diario_por_horas_en_porciento_semana_18_30[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)

    #semana_31_43_pico=pico_maximo_por_dias[210:301]#--------------------------------------------------
            
    for i in pico_maximo_por_dias[210:215]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[215:217]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[217:222]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[222:224]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[224:229]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[229:231]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[231:236]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[236:238]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[238:243]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[243:245]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[245:250]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[250:252]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[252:257]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[257:259]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[259:264]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[264:266]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[266:271]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[271:273]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[273:278]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[278:280]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[280:285]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[285:287]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[287:292]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[292:294]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[294:299]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[299:301]:
        for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
            
    #semana_44_52_pico=pico_maximo_por_dias[301:364]#----------------------------------------------------------------------
        
    for i in pico_maximo_por_dias[301:306]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[306:308]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[308:313]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[313:315]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[315:320]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[320:322]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[322:327]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[327:329]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[329:334]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[334:336]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[336:341]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[341:343]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[343:348]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[348:350]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[350:355]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[355:357]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[357:362]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[0:24]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    for i in pico_maximo_por_dias[362:364]:
        for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:48]:
            solv1=i*(j/100)
            pico_diario.append(solv1)
    print(pico_diario,len(pico_diario))
   
    # Graficar la lista
    plt.plot(pico_diario)
    # Mostrar el gráfico
    plt.show()
    return pico_diario
#!Calcular el valor de los datos ---MTTR y MTTF------------------------------------------------------------------------

#todo CALCULANDO PRIMERAMENTE LOS VALORES DE MTTF, la generacion de los datos tiene que ser menor que 8784
# TODOb datos que son los valores que se obtuvieron en la curva de caraga

#TODO  Extraer la columna y convertirla en una lista sobre los datos de MTTF
def Parametros_para_MTTF_MTTR(Nombre_excel:str,MTTF:str, MTTR:str):
        #! Establecer la recoleccion de datos de la tabla_4_---------------------------------------------------

    # Obtiene la ruta del directorio actual donde se encuentra el script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Especifica el nombre del archivo XLSX
    nombre_archivo = Nombre_excel

    # Une la ruta del directorio actual con el nombre del archivo
    ruta_archivo_xlsx = os.path.join(directorio_actual, nombre_archivo)

    # Lee el archivo XLSX y carga sus datos en un DataFrame de pandas
    df = pd.read_excel(nombre_archivo, engine='openpyxl')

    # Ahora 'df' contiene los datos del archivo XLSX en forma de DataFrame
    # Puedes imprimir el DataFrame para verificar
    # print(df)
    lista_columna_MTTF = df[MTTF].tolist()
    lista_paramet_dis_exp_de_MTTF=[]
    lista_paramet_dis_exp_de_MTTR=[]
    # TODO La taza de falla es igual que el medio tiempo hasta el fallo,por tanto
    # TODO se puede calcular el parametro de la distribucion exponencial
    for i in  lista_columna_MTTF:
        parametro_dist_exp=1/i #Parámetro Distribución Exponencial
        lista_paramet_dis_exp_de_MTTF.append(parametro_dist_exp)
    # TODO Extraer la columna y convertirla en una lista sobre los datos de MTTR
    lista_columna_MTTR = df[MTTR].tolist()
    lista_paramet_dis_exp_de_MTTR=[]
    for i in  lista_columna_MTTR:
        parametro_dist_exp=1/i #Parámetro Distribución Exponencial
        lista_paramet_dis_exp_de_MTTR.append(parametro_dist_exp)
    print('lista_paramet_dis_exp_de_MTTR',lista_paramet_dis_exp_de_MTTR)
    print('lista_paramet_dis_exp_de_MTTF',lista_paramet_dis_exp_de_MTTF)
# * Calculo de los valores aleatorios y los tiempos para TTF y TTR -----------------------------------------------------
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
    print("\n==================A CONTINUACION LOS TIEMPOS DE FALLA=======================================================\n")
    print('tiempos_de_falla_U12=',tiempos_de_falla_U12)    
    print('tiempos_de_falla_U20=',tiempos_de_falla_U20)    
    print('tiempos_de_falla_U50=',tiempos_de_falla_U50)    
    print('tiempos_de_falla_U76=',tiempos_de_falla_U76)    
    print('tiempos_de_falla_U100=',tiempos_de_falla_U100)
    print('tiempos_de_falla_U155=',tiempos_de_falla_U155)
    print('tiempos_de_falla_U197=',tiempos_de_falla_U197)
    print('tiempos_de_falla_U350=',tiempos_de_falla_U350)
    print('tiempos_de_falla_U400=',tiempos_de_falla_U400)
    print("\n==================A CONTINUACION LOS TIEMPOS DE REPARCION=======================================================\n")
    print('tiempos_de_reparacion_U12=',tiempos_de_reparacion_U12)    
    print('tiempos_de_reparacion_U20=',tiempos_de_reparacion_U20)    
    print('tiempos_de_reparacion_U50=',tiempos_de_reparacion_U50)    
    print('tiempos_de_reparacion_U76=',tiempos_de_reparacion_U76)    
    print('tiempos_de_reparacion_U100=',tiempos_de_reparacion_U100)
    print('tiempos_de_reparacion_U155=',tiempos_de_reparacion_U155)
    print('tiempos_de_reparacion_U197=',tiempos_de_reparacion_U197)
    print('tiempos_de_reparacion_U350=',tiempos_de_reparacion_U350)
    print('tiempos_de_reparacion_U400=',tiempos_de_reparacion_U400)
    
    return lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,tiempos_de_falla_U12,tiempos_de_falla_U20,tiempos_de_falla_U50,tiempos_de_falla_U76,tiempos_de_falla_U100,tiempos_de_falla_U155,tiempos_de_falla_U197,tiempos_de_falla_U350,tiempos_de_falla_U400,tiempos_de_reparacion_U12,tiempos_de_reparacion_U20,tiempos_de_reparacion_U50,tiempos_de_reparacion_U76,tiempos_de_reparacion_U100,tiempos_de_reparacion_U155,tiempos_de_reparacion_U197,tiempos_de_reparacion_U350,tiempos_de_reparacion_U400

# #TODO degradation_de las Unidades_sin_mantenimiento
def funcion_escalon(ttf, ttr,valor_max_MW:int):
    tiempo_total = 8761
    resultado = []
    acumulado = 0
    escalon_actual = valor_max_MW
    for i,j in zip(sorted(ttf),sorted(ttr)):
            acumulado+=i
            resultado.extend([escalon_actual] * int(i))
            acumulado+=j
            resultado.extend([0] * int(acumulado))
            if acumulado>=8761:
                        break
            else:continue
    plt.plot(range(len(resultado)), resultado)
    plt.xlabel('Tiempo')
    plt.ylabel('Valor del escalón')
    plt.title('Función Escalón')
    plt.show()
    return resultado