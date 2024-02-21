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
    import matplotlib.pyplot as plt
    # Graficar la lista
    plt.plot(pico_diario)
    # Mostrar el gráfico
    plt.show()
    return pico_diario



#! Comprobacion de los datos suministrados a la tabla
#suma=[]
# suma.append(len(pico_maximo_por_dias[0:5]))
# suma.append(len(pico_maximo_por_dias[5:7]))
# suma.append(len(pico_maximo_por_dias[7:12]))
# suma.append(len(pico_maximo_por_dias[12:14]))
# suma.append(len(pico_maximo_por_dias[14:19]))
# suma.append(len(pico_maximo_por_dias[19:21]))
# suma.append(len(pico_maximo_por_dias[21:26]))
# suma.append(len(pico_maximo_por_dias[26:28]))
# suma.append(len(pico_maximo_por_dias[28:33]))
# suma.append(len(pico_maximo_por_dias[33:35]))
# suma.append(len(pico_maximo_por_dias[35:40]))
# suma.append(len(pico_maximo_por_dias[40:42]))
# suma.append(len(pico_maximo_por_dias[42:47]))
# suma.append(len(pico_maximo_por_dias[47:49]))
# suma.append(len(pico_maximo_por_dias[49:54]))
# suma.append(len(pico_maximo_por_dias[54:56]))
# suma.append(len(pico_maximo_por_dias[56:61]))
# suma.append(len(pico_maximo_por_dias[61:63]))
# suma.append(len(pico_maximo_por_dias[63:68]))
# suma.append(len(pico_maximo_por_dias[68:70]))
# suma.append(len(pico_maximo_por_dias[70:75]))
# suma.append(len(pico_maximo_por_dias[75:77]))
# suma.append(len(pico_maximo_por_dias[77:82]))
# suma.append(len(pico_maximo_por_dias[82:84]))
# suma.append(len(pico_maximo_por_dias[84:89]))
# suma.append(len(pico_maximo_por_dias[89:91]))
# suma.append(len(pico_maximo_por_dias[91:96]))
# suma.append(len(pico_maximo_por_dias[96:98]))
# suma.append(len(pico_maximo_por_dias[98:103]))
# suma.append(len(pico_maximo_por_dias[103:105]))
# suma.append(len(pico_maximo_por_dias[105:110]))
# suma.append(len(pico_maximo_por_dias[110:112]))
# suma.append(len(pico_maximo_por_dias[112:117]))
# suma.append(len(pico_maximo_por_dias[117:119]))
# suma.append(len(pico_maximo_por_dias[119:124]))
# suma.append(len(pico_maximo_por_dias[124:126]))
# suma.append(len(pico_maximo_por_dias[126:131]))
# suma.append(len(pico_maximo_por_dias[131:133]))
# suma.append(len(pico_maximo_por_dias[133:138]))
# suma.append(len(pico_maximo_por_dias[138:140]))
# suma.append(len(pico_maximo_por_dias[140:145]))
# suma.append(len(pico_maximo_por_dias[145:147]))
# suma.append(len(pico_maximo_por_dias[147:152]))
# suma.append(len(pico_maximo_por_dias[152:154]))
# suma.append(len(pico_maximo_por_dias[154:159]))
# suma.append(len(pico_maximo_por_dias[159:161]))
# suma.append(len(pico_maximo_por_dias[161:166]))
# suma.append(len(pico_maximo_por_dias[166:168]))
# suma.append(len(pico_maximo_por_dias[168:173]))
# suma.append(len(pico_maximo_por_dias[173:175]))
# suma.append(len(pico_maximo_por_dias[175:180]))
# suma.append(len(pico_maximo_por_dias[180:182]))
# suma.append(len(pico_maximo_por_dias[182:187]))
# suma.append(len(pico_maximo_por_dias[187:189]))
# suma.append(len(pico_maximo_por_dias[189:194]))
# suma.append(len(pico_maximo_por_dias[194:196]))
# suma.append(len(pico_maximo_por_dias[196:201]))
# suma.append(len(pico_maximo_por_dias[201:203]))
# suma.append(len(pico_maximo_por_dias[203:208]))
# suma.append(len(pico_maximo_por_dias[208:210]))
# suma.append(len(pico_maximo_por_dias[210:215]))
# suma.append(len(pico_maximo_por_dias[215:217]))
# suma.append(len(pico_maximo_por_dias[217:222]))
# suma.append(len(pico_maximo_por_dias[222:224]))
# suma.append(len(pico_maximo_por_dias[224:229]))
# suma.append(len(pico_maximo_por_dias[229:231]))
# suma.append(len(pico_maximo_por_dias[231:236]))
# suma.append(len(pico_maximo_por_dias[236:238]))
# suma.append(len(pico_maximo_por_dias[238:243]))
# suma.append(len(pico_maximo_por_dias[243:245]))
# suma.append(len(pico_maximo_por_dias[245:250]))
# suma.append(len(pico_maximo_por_dias[250:252]))
# suma.append(len(pico_maximo_por_dias[252:257]))
# suma.append(len(pico_maximo_por_dias[257:259]))
# suma.append(len(pico_maximo_por_dias[259:264]))
# suma.append(len(pico_maximo_por_dias[264:266]))
# suma.append(len(pico_maximo_por_dias[266:271]))
# suma.append(len(pico_maximo_por_dias[271:273]))
# suma.append(len(pico_maximo_por_dias[273:278]))
# suma.append(len(pico_maximo_por_dias[278:280]))
# suma.append(len(pico_maximo_por_dias[280:285]))
# suma.append(len(pico_maximo_por_dias[285:287]))
# suma.append(len(pico_maximo_por_dias[287:292]))
# suma.append(len(pico_maximo_por_dias[292:294]))
# suma.append(len(pico_maximo_por_dias[294:299]))
# suma.append(len(pico_maximo_por_dias[299:301]))
# suma.append(len(pico_maximo_por_dias[301:306]))
# suma.append(len(pico_maximo_por_dias[306:308]))
# suma.append(len(pico_maximo_por_dias[308:313]))
# suma.append(len(pico_maximo_por_dias[313:315]))
# suma.append(len(pico_maximo_por_dias[315:320]))
# suma.append(len(pico_maximo_por_dias[320:322]))
# suma.append(len(pico_maximo_por_dias[322:327]))
# suma.append(len(pico_maximo_por_dias[327:329]))
# suma.append(len(pico_maximo_por_dias[329:334]))
# suma.append(len(pico_maximo_por_dias[334:336]))
# suma.append(len(pico_maximo_por_dias[336:341]))
# suma.append(len(pico_maximo_por_dias[341:343]))
# suma.append(len(pico_maximo_por_dias[343:348]))
# suma.append(len(pico_maximo_por_dias[348:350]))
# suma.append(len(pico_maximo_por_dias[350:355]))
# suma.append(len(pico_maximo_por_dias[355:357]))
# suma.append(len(pico_maximo_por_dias[357:362]))
# suma.append(len(pico_maximo_por_dias[362:364]))

# print(sum(suma))


