 #**********************************************LIBRERIAS UTILIZADAS*********************************************************
import matplotlib.pyplot as plt
from scipy.stats import expon
import pandas as pd
import os
import sympy as sp
import numpy as np
import random
import matplotlib.pyplot as plt
from random import Random
from time import time
import inspyred
import math
#***********************************************************Calculo_de_la_demanda******************************************************************
def calculo_demanda(pico_maximo:int,pico_maximo_por_semana_en_porciento:list,
                    pico_maximo_por_dias_en_porciento:int,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52:list,
                    pico_diario_por_horas_en_porciento_semana_18_30:list,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43:list):
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
    return pico_diario
#*********************************************************Calculo_de_los_valores_MTTR_MTTF_********************************************************
#TODO_CALCULANDO PRIMERAMENTE LOS VALORES DE MTTF, la generacion de los datos tiene que ser menor que 8784
#TODO_datos que son los valores que se obtuvieron en la curva de caraga
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
    # print('lista_paramet_dis_exp_de_MTTR',lista_paramet_dis_exp_de_MTTR)
    # print('lista_paramet_dis_exp_de_MTTF',lista_paramet_dis_exp_de_MTTF)
    return lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR
#******************************************************Funcion_escalon_para_encontrar_ttr_ttf******************************************************

def calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF_o_MTTR, n, valores_randon):
    tiempos_de_falla_o_repracion = []
    
    for _ in range(valores_randon):
        resultado_en_tasa = expon.ppf(lista_paramet_dis_exp_de_MTTF_o_MTTR[n], np.random.rand()*4)
        resultado_en_horas = resultado_en_tasa / lista_paramet_dis_exp_de_MTTF_o_MTTR[n]  # Corrección
        # print('resultado_en_hora_ttf =', resultado_en_horas)
        
        tiempos_de_falla_o_repracion.append(resultado_en_horas)
        
        if sum(tiempos_de_falla_o_repracion) <= 8736:
            continue
        else:
            break
    
    return tiempos_de_falla_o_repracion
#***************************************************Funcion_Escalon*******************************************************************************
def funcion_escalon(ttf, ttr, valor_max_MW: int):
    tiempo_total = 8736
    resultado = []
    acumulado = 0
    escalon_actual = valor_max_MW
    for i, j in zip(sorted(ttf), sorted(ttr)):
# Mantener el escalón en valor_max_MW hasta el primer valor de ttf
        resultado.extend([escalon_actual] * int(i))
        acumulado += i
# Caer a cero durante el tiempo de ttr
        resultado.extend([0] * int(j))
        acumulado += j
        escalon_actual = valor_max_MW  # Volver a subir a valor_max_MW al llegar al último valor de ttr
        if acumulado >= tiempo_total:
            break
    return resultado
#*******************************************Funcion_de_subplot************************************************************************************
def crear_subplot(indice, datos, etiqueta):
    plt.subplot(6,6 , indice)
    plt.plot(range(len(datos)), datos)
    plt.title(f'UNIDAD {etiqueta}',fontsize=5)
    plt.xlabel('Tiempo',fontsize=5)
    plt.ylabel('Valor del escalón',fontsize=5)
#******************************************Funcion_de_Mantenimiento*******************************************************************************
def funcion_de_mantenimiento(semanas_de_mant_por_dato: int, semanas_entre_mantenimiento: int, valor_en_MW, inicio_mantenimiento_hora_year: int = 0):
    try:
        lista = [valor_en_MW] * 8736
        horas_entre_mantenimiento = semanas_de_mant_por_dato * 24
        contador = 0
# Asegurar que semanas_de_mant_por_dato no sea mayor que la cantidad total de semanas en el año
        semanas_en_ano = 52
        if semanas_de_mant_por_dato > semanas_en_ano:
            raise ValueError("La cantidad de semanas de mantenimiento no puede ser mayor que la cantidad total de semanas en el año.")
# Asegurar que el espacio entre mantenimientos sea válido
        if semanas_entre_mantenimiento * 7 * 24 >= len(lista):
            raise ValueError("El espacio entre mantenimientos excede la longitud de la lista. Por favor, ingrese nuevos valores.")
        inicio_mantenimiento_indice = inicio_mantenimiento_hora_year % len(lista)
        for _ in range(semanas_de_mant_por_dato):
# Establecer mantenimiento en las próximas semanas
            if semanas_entre_mantenimiento!=0:
                for i in range(horas_entre_mantenimiento):
                 lista[(contador + inicio_mantenimiento_indice + i) % len(lista)] = 0
# Restablecer el valor_en_MW después de las semanas de mantenimiento
            lista[(contador + inicio_mantenimiento_indice + horas_entre_mantenimiento) % len(lista)] = valor_en_MW

            contador += horas_entre_mantenimiento + 1  # Moverse a la próxima posición después del mantenimiento
# Actualizar el índice de inicio para la próxima semana de mantenimiento
            inicio_mantenimiento_indice += semanas_entre_mantenimiento * 7 * 24
        return lista
    except ValueError as e:
        print(f"Error: {e}")
        raise  # Re-levanta la excepción para que el usuario pueda ingresar nuevos valores
#*******************************AND ENTRE VALORES************************************************************************************************
def AND_entre_valores(valores1, valores2, unidad_en_MW):
    vector_resultante = []
# Verifica que ambas listas tengan la misma longitud
    if len(valores1) != len(valores2):
       raise ValueError("Las listas deben tener la misma longitud")
    for v1, v2 in zip(valores1, valores2):
        resultado_and = v1 and v2
        if resultado_and:
            vector_resultante.append(unidad_en_MW)
        else:
            vector_resultante.append(0)
    print("Resultado de la operación AND con valores específicos:", vector_resultante)
    return vector_resultante

#******************************Algoritmo Genetico para minimizar la solucion del problema *******************************************************
# def main(problema, prng=None, display=False):    
#     if prng is None:
#         prng = Random()
#         prng.seed(time())
        
#     points = [(110.0, 225.0), (161.0, 280.0), (325.0, 554.0), (490.0, 285.0),
#               (157.0, 443.0), (283.0, 379.0), (397.0, 566.0), (306.0, 360.0),
#               (343.0, 110.0), (552.0, 199.0)]
#     weights = [[0 for _ in range(len(points))] for _ in range(len(points))]
#     for i, p in enumerate(points):
#         for j, q in enumerate(points):
#             weights[i][j] = math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
              
#     problem = inspyred.benchmarks.TSP(weights)
#     ea = inspyred.ec.EvolutionaryComputation(prng)
#     ea.selector = inspyred.ec.selectors.tournament_selection
#     ea.variator = [inspyred.ec.variators.partially_matched_crossover, 
#                    inspyred.ec.variators.inversion_mutation]
#     ea.replacer = inspyred.ec.replacers.generational_replacement
#     ea.terminator = inspyred.ec.terminators.generation_termination
#     final_pop = ea.evolve(generator=problem.generator, 
#                           evaluator=evaluador, 
#                           bounder=problem.bounder,
#                           maximize=False, 
#                           pop_size=100, 
#                           max_generations=50,
#                           tournament_size=5,
#                           num_selected=100,
#                           num_elites=1)
    
#     if display:
#         best = min(ea.population)
#         return best.candidate
            
# def evaluador(candidato):
#     return problema(candidato),

# if __name__ == '__main__':
#     def problema(x):
#         # Definir tu problema de minimización aquí
#         # La función debe devolver el valor de la función objetivo a minimizar
#         # basado en los valores de las variables de decisión en la lista `x`
#         pass
    
#     resultado = main(problema, display=True)
#     print('Mejor Solución:', resultado)
#**********************************FUNCION DE Riesgo Utilizando montecarlos***********************************************************************
def riesgo(demanda:list,generacion:list):
    #print(len(demanda),len(generacion))
    riesgo=[]
    for i,j in zip(demanda,generacion):
        if j>=i:
            solv=0
            riesgo.append(solv)
        if i>=j:
            solv=i-j
            riesgo.append(solv)
    suma_de_riesgo=sum(riesgo)
    print('suma_de_riesgo=',suma_de_riesgo)
    return suma_de_riesgo

def error(suma_de_riesgo:float,pico_diario):
#?calculo de varianza en este caso para establecer el patron de parada segun montecarlos 
    vector_riesgo=[]
    error=[]
    while  True:
        if suma_de_riesgo==0:
            vector_riesgo.append(0)
            valor_esperado_riesgo = np.mean(vector_riesgo)
            error=None
            generacion=Simulacion()
            riesgo(pico_diario,generacion)
            continue
        elif suma_de_riesgo!=0:
            vector_riesgo.append(suma_de_riesgo)
            valor_esperado_riesgo = np.mean(vector_riesgo)
            desviacion_estandar = np.std(vector_riesgo)
            error=desviacion_estandar/(valor_esperado_riesgo*math.sqrt(len(vector_riesgo)))
#?Valor del error para el criterio de parada
            if error<=0.01 and desviacion_estandar>0:
                print("el valor_esperado_riesgo del valor de riesgo es:> ",valor_esperado_riesgo)
                print('error>',error)
                break
            # print('error>',error)
            # print(f'el valor esperado es de {valor_esperado_riesgo} MW')
            generacion=Simulacion()
            riesgo(pico_diario,generacion)
    return valor_esperado_riesgo,error

#**************************************************************************************************Funcion de Simulacion completada*********************************
def Simulacion():
    #! Calculo de los valores TTR y TTF de las variables aleatorias en casda caso =================================================================================
    MTTF='MTTF(horas)'
    MTTR='MTTR(horas)'
    Nombre_excel='Tabla4_IEEE.xlsx' # el excel debe estar dentro de la misma carpeta

    Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)


    #TODO degradation_de las Unidades_sin_mantenimiento
    lista_paramet_dis_exp_de_MTTF,lista_paramet_dis_exp_de_MTTR,=Parametros_para_MTTF_MTTR(Nombre_excel,MTTF,MTTR)

#***************************Valores de ttf aleatorios **************************\n'
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,0,100)#U12
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,1,100)#U20
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,2,100)#U50
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,3,100)#U76
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,4,100)#U100
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,5,100)#U155
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,6,100)#U197
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,7,100)#U350
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTF,8,100)#U400
#***************************Valores de ttr aleatorios**************************\n')
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,0,100)#)U12
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,1,100)#U20
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,2,100)#U50
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,3,100)#U76
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,4,100)#)U100
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,5,100)#)U155
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,6,100)#)U197
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,7,100)#)U350
    calulo_ttf_ttr(lista_paramet_dis_exp_de_MTTR,8,100)#U400
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
#*#########################################Semanas de Mant*dias_de_la_Semana*horas del dia**********************************************
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
    MANT_U12_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_12,0,12,4434)
    MANT_U12_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_12,0,12,2015)
    MANT_U12_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_12,0,12,5512)
    MANT_U12_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_12,0,12,970)
    MANT_U12_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_12,0,12,5959)
    MANT_U20_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_20,0,20,3006)
    MANT_U20_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_20,0,20,7)
    MANT_U20_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_20,0,20,5002)
    MANT_U20_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_20,0,20,1872)
    MANT_U50_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_50,0,50,7248)
    MANT_U50_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_50,0,50,5540)
    MANT_U50_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_50,0,50,5043)
    MANT_U50_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_50,0,50,4331)
    MANT_U50_5=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_50,0,50,1809)
    MANT_U50_6=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_6U_50,0,50,6514)
    MANT_U76_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_76,0,76,1305)
    MANT_U76_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_76,0,76,1828)
    MANT_U76_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_76,0,76,5041)
    MANT_U76_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_76,0,76,5523)
    MANT_U100_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_100,0,100,6719)
    MANT_U100_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_100,0,100,6376)
    MANT_U100_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_100,0,100,327)
    MANT_U155_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_155,0,155,3317)
    MANT_U155_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_155,0,155,7885)
    MANT_U155_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_155,0,155,7257)
    MANT_U155_4=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_155,0,155,2527)
    MANT_U197_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_197,0,197,1849)
    MANT_U197_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_197,0,197,4222)
    MANT_U197_3=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_197,0,197,4318)
    MANT_U350_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_350,0,350,5072)
    MANT_U400_1=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_400,0,400,405)
    MANT_U400_2=funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_400,0,400,4190)
        
    #*Desarrollo de un AND para la union de los mantenimientos y los estados de degradaion
    #**********************************UNIDAD 12 *************************
    AND_U12_1=AND_entre_valores(valores_acotados_ventana_1U12,MANT_U12_1,12)
    AND_U12_2=AND_entre_valores(valores_acotados_ventana_2U12,MANT_U12_2,12)
    AND_U12_3=AND_entre_valores(valores_acotados_ventana_3U12,MANT_U12_3,12)
    AND_U12_4=AND_entre_valores(valores_acotados_ventana_4U12,MANT_U12_4,12)
    AND_U12_5=AND_entre_valores(valores_acotados_ventana_5U12,MANT_U12_5,12)
    #**********************************UNIDAD 20 *************************
    AND_U20_1=AND_entre_valores(valores_acotados_ventana_1U20,MANT_U20_1,20)
    AND_U20_2=AND_entre_valores(valores_acotados_ventana_2U20,MANT_U20_2,20)
    AND_U20_3=AND_entre_valores(valores_acotados_ventana_3U20,MANT_U20_3,20)
    AND_U20_4=AND_entre_valores(valores_acotados_ventana_4U20,MANT_U20_4,20)
    #**********************************UNIDAD 50 *************************
    AND_U50_1=AND_entre_valores(valores_acotados_ventana_1U50,MANT_U50_1,50)
    AND_U50_2=AND_entre_valores(valores_acotados_ventana_2U50,MANT_U50_2,50)
    AND_U50_3=AND_entre_valores(valores_acotados_ventana_3U50,MANT_U50_3,50)
    AND_U50_4=AND_entre_valores(valores_acotados_ventana_4U50,MANT_U50_4,50)
    AND_U50_5=AND_entre_valores(valores_acotados_ventana_5U50,MANT_U50_5,50)
    AND_U50_6=AND_entre_valores(valores_acotados_ventana_6U50,MANT_U50_6,50)
    # Ajustar el diseño para evitar superposiciones
    #**********************************UNIDAD 76 *************************
    AND_U76_1=AND_entre_valores(valores_acotados_ventana_1U76,MANT_U76_1,76)
    AND_U76_2=AND_entre_valores(valores_acotados_ventana_2U76,MANT_U76_2,76)
    AND_U76_3=AND_entre_valores(valores_acotados_ventana_3U76,MANT_U76_3,76)
    AND_U76_4=AND_entre_valores(valores_acotados_ventana_4U76,MANT_U76_4,76)

    #**********************************UNIDAD 100 *************************
    AND_U100_1=AND_entre_valores(valores_acotados_ventana_1U100,MANT_U100_1,100)
    AND_U100_2=AND_entre_valores(valores_acotados_ventana_2U100,MANT_U100_2,100)
    AND_U100_3=AND_entre_valores(valores_acotados_ventana_3U100,MANT_U100_3,100)
    #**********************************UNIDAD 155 *************************
    AND_U155_1=AND_entre_valores(valores_acotados_ventana_1U155,MANT_U155_1,155)
    AND_U155_2=AND_entre_valores(valores_acotados_ventana_2U155,MANT_U155_2,155)
    AND_U155_3=AND_entre_valores(valores_acotados_ventana_3U155,MANT_U155_3,155)
    AND_U155_4=AND_entre_valores(valores_acotados_ventana_4U155,MANT_U155_4,155)
    #**********************************UNIDAD 197 *************************
    AND_U197_1=AND_entre_valores(valores_acotados_ventana_1U197,MANT_U197_1,197)
    AND_U197_2=AND_entre_valores(valores_acotados_ventana_2U197,MANT_U197_2,197)
    AND_U197_3=AND_entre_valores(valores_acotados_ventana_3U197,MANT_U197_3,197)
    #**********************************UNIDAD 350 *************************
    AND_U350_1=AND_entre_valores(valores_acotados_ventana_1U350,MANT_U350_1,350)
    #**********************************UNIDAD 400 *************************
    AND_U400_1=AND_entre_valores(valores_para_acotar_la_ventana_1U400,MANT_U400_1,400)
    AND_U400_2=AND_entre_valores(valores_para_acotar_la_ventana_2U400,MANT_U400_2,400)
   
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
    return resultado_suma
