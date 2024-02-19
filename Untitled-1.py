
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
pico_diario_por_horas_en_porciento_semana_18_30=[64,60,58,56,56,58,64,76,87,95,99,100,99,100,100,97,96,96,93,92,92,93,87,72,
                                                 74,70,66,65,64,62,62,66,81,86,91,93,93,92,91,91,92,94,95,95,100,93,88,80]                                   
pico_diario_por_horas_en_porciento_semana_9_17_y_31_43=[63,62,60,58,59,65,72,85,95,99,100,99,93,92,90,88,90,92,96,98,96,90,80,70,
                                                        75,73,69,66,65,65,68,74,83,89,92,94,91,90,90,86,85,88,92,100,97,95,90,85]                                                         

# def calculo_demanda(pico_maximo:int,pico_maximo_por_semana_en_porciento:list,pico_maximo_por_dias_en_porciento:int,pico_diario_por_horas_en_porciento_semana_1_8_y_44_52:list,pico_diario_por_horas_en_porciento_semana_18_30:list,pico_diario_por_horas_en_porciento_semana_9_17_y_31_43:list)
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
semana_1_8_picos=pico_maximo_por_dias[:63]

for i in pico_maximo_por_dias[:5]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[5:7]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[7:12]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[12:14]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[14:19]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[19:21]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[21:26]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[26:28]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[28:33]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[33:35]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[35:40]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[40:42]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[42:47]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[47:49]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[49:54]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[54:56]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[56:61]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[61:63]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
        
semana_9_17_pico=pico_maximo_por_dias[63:126]#----------------------------------------------------------------------


for i in pico_maximo_por_dias[61:63]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[63:68]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[68:70]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[70:75]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[75:77]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[77:82]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[82:84]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[84:89]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[89:91]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[91:96]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[96:98]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[98:103]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[103:105]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[105:110]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[110:112]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[112:117]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[117:119]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[119:124]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[124:126]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)

semana_18_30_pico=pico_maximo_por_dias[126:217]#----------------------------------------------------------------------


for i in pico_maximo_por_dias[126:131]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[131:133]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[133:138]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[138:140]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[140:145]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[145:147]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[147:152]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[152:157]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[157:162]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[162:164]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[164:169]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[169:171]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[171:176]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[176:178]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[178:183]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[183:185]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[185:187]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[187:189]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[189:194]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[194:196]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[196:201]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[201:203]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[203:208]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[208:210]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[210:215]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[215:217]:
    for j in pico_diario_por_horas_en_porciento_semana_18_30[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)

semana_31_43_pico=pico_maximo_por_dias[217:308]#--------------------------------------------------
        

for i in pico_maximo_por_dias[217:222]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[222:224]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[224:229]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[229:231]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[231:236]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[236:238]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[238:243]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[243:245]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[245:250]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[250:252]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[252:257]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[257:259]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[259:264]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[264:266]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[266:271]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[271:273]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[273:278]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[278:280]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[280:285]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[285:287]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[287:292]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[292:294]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[294:299]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[299:301]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[301:306]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[306:308]:
    for j in pico_diario_por_horas_en_porciento_semana_9_17_y_31_43[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)

semana_44_52_pico=pico_maximo_por_dias[308:364]
for i in pico_maximo_por_dias[308:313]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[313:315]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[315:320]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[320:322]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[322:327]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[327:329]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[329:334]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[334:336]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[336:341]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[341:343]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[343:348]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[348:350]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[350:355]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[355:357]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[357:362]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[:24]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
for i in pico_maximo_por_dias[362:364]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
print(pico_diario,len(pico_diario))
        
        
        
        
        
        
        
        
# return pico_diario