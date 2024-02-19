 #!Encontrar el pico de la demanda---------------------------------------------
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
                                                         
#calculo a paritr de los picos maximos
#? Variables para el calculo 
pico_maximo_por_semana=[]
pico_maximo_por_dias=[]
pico_diario=[]
# Funcion para el calculo de la demadna 

# # def calculo_demanda()
for i in pico_maximo_por_semana_en_porciento:
    resultado=(pico_maximo*(i/100))
    pico_maximo_por_semana.append(resultado)
    
for i in pico_maximo_por_semana :
        for j in pico_maximo_por_dias_en_porciento:
            resultado1= i *(j/100)
            pico_maximo_por_dias.append(resultado1)
            
semana_1_8_picos=pico_maximo_por_dias[:57]


#TODo Primer grupo de valores para el calculo de la demanda--------------------------------------
semana_1_8_picos=pico_maximo_por_dias[:57]
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
print(pico_diario,len(pico_diario))


semana_9_17_pico=pico_maximo_por_dias[56:64]#----------------------------------------------------------------------

for i in pico_maximo_por_dias[56:56]:
    for j in pico_diario_por_horas_en_porciento_semana_1_8_y_44_52[24:]:
        solv1=i*(j/100)
        pico_diario.append(solv1)
print(pico_diario,len(pico_diario))




# 
# semana9_17_datos_dados=pico_diario_por_horas_en_porciento[24:49]
# for i in  semana_9_17_pico:
#     for j in semana9_17_datos_dados:
#         solv2=i*j
#         pico_diario.append(solv2) 
        
# semana_18_30_pico=pico_maximo_por_dias[119:211]
# semana_18_30_datos_dados=pico_diario_por_horas_en_porciento[48:73]
# for i in  semana_18_30_pico:
#     for j in semana_18_30_datos_dados:
#         solv3=i*j
#         pico_diario.append(solv3) 
        
# semana_31_43_pico=pico_maximo_por_dias[210:302]
# semana_31_43__datos_dados=pico_diario_por_horas_en_porciento[72:97]
# for i in  semana_31_43_pico:
#     for j in semana_31_43__datos_dados:
#         solv3=i*j
#         pico_diario.append(solv3) 
        
# semana_44_52_pico=pico_maximo_por_dias[301:365]
# semana_31_43__datos_dados=pico_diario_por_horas_en_porciento[98:123]
# for i in  semana_44_52_pico:
#     for j in semana_31_43__datos_dados:
#         solv3=i*j
#         pico_diario.append(solv3)
        
# 