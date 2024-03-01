def Simulacion():
    from New_script_funciones import *
    from Modelo_Optimizacion import *
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
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_12,1,12)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_12,3,12)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_12,3,12)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_12,3,12)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_12,3,12)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_20,3,20)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_20,3,20)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_20,3,20)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_20,3,20)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_6U_50,5,50)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_76,2,76)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_76,2,76)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_76,2,76)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_76,2,76)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_100,2,100)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_100,2,100)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_100,2,100)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_155,2,155)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_155,2,155)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_155,2,155)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_155,2,155)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_197,3,197)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_197,3,197)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_197,3,197)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_350,1,350)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_400,1,400)
    funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_400,1,400)
    AND_entre_valores(valores_acotados_ventana_1U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_12,5,12),12)
    AND_entre_valores(valores_acotados_ventana_2U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_12,3,12),12)
    AND_entre_valores(valores_acotados_ventana_3U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_12,3,12),12)
    AND_entre_valores(valores_acotados_ventana_4U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_12,3,12),12)
    AND_entre_valores(valores_acotados_ventana_5U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_12,3,12),12)
    AND_entre_valores(valores_acotados_ventana_1U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_20,3,20),20)
    AND_entre_valores(valores_acotados_ventana_2U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_20,3,20),20)
    AND_entre_valores(valores_acotados_ventana_3U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_20,3,20),20)
    AND_entre_valores(valores_acotados_ventana_4U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_20,3,20),20)
    AND_entre_valores(valores_acotados_ventana_1U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_2U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_3U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_4U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_5U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_6U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_6U_50,5,50),50)
    AND_entre_valores(valores_acotados_ventana_1U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_76,2,76),76)
    AND_entre_valores(valores_acotados_ventana_2U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_76,2,76),76)
    AND_entre_valores(valores_acotados_ventana_3U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_76,2,76),76)
    AND_entre_valores(valores_acotados_ventana_4U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_76,2,76),76)
    AND_entre_valores(valores_acotados_ventana_1U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_100,2,100),100)
    AND_entre_valores(valores_acotados_ventana_2U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_100,2,100),100)
    AND_entre_valores(valores_acotados_ventana_3U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_100,2,100),100)
    AND_entre_valores(valores_acotados_ventana_1U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_155,2,155),155)
    AND_entre_valores(valores_acotados_ventana_2U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_155,2,155),155)
    AND_entre_valores(valores_acotados_ventana_3U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_155,2,155),155)
    AND_entre_valores(valores_acotados_ventana_4U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_155,2,155),155)
    AND_entre_valores(valores_acotados_ventana_1U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_197,3,197),197)
    AND_entre_valores(valores_acotados_ventana_2U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_197,3,197),197)
    AND_entre_valores(valores_acotados_ventana_3U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_197,3,197),197)
    AND_entre_valores(valores_acotados_ventana_1U350,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_350,1,350),350)
    AND_entre_valores(valores_para_acotar_la_ventana_1U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_400,1,400),400)
    AND_entre_valores(valores_para_acotar_la_ventana_2U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_400,1,400),400)
    resultado_suma = [a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+ab+cd+ef+gh+ij+kl for a,bc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,abcd,ef,gh,ij,kl in zip(AND_entre_valores(valores_acotados_ventana_1U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_12,5,12),12),AND_entre_valores(valores_acotados_ventana_2U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_12,3,12),12),AND_entre_valores(valores_acotados_ventana_3U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_12,3,12),12),AND_entre_valores(valores_acotados_ventana_4U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_12,3,12),12),AND_entre_valores(valores_acotados_ventana_5U12,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_12,3,12),12),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_20,3,20),20),AND_entre_valores(valores_acotados_ventana_2U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_20,3,20),20),AND_entre_valores(valores_acotados_ventana_3U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_20,3,20),20),AND_entre_valores(valores_acotados_ventana_4U20,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_20,3,20),20),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_50,3,50),50),AND_entre_valores(valores_acotados_ventana_2U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_50,3,50),50),AND_entre_valores(valores_acotados_ventana_3U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_50,3,50),50),AND_entre_valores(valores_acotados_ventana_4U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_50,3,50),50),AND_entre_valores(valores_acotados_ventana_5U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_5U_50,3,50),50),AND_entre_valores(valores_acotados_ventana_6U50,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_6U_50,3,50),50),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_76,2,76),76),AND_entre_valores(valores_acotados_ventana_2U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_76,2,76),76),AND_entre_valores(valores_acotados_ventana_3U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_76,2,76),76),AND_entre_valores(valores_acotados_ventana_4U76,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_76,2,76),76),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_100,2,100),100),AND_entre_valores(valores_acotados_ventana_2U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_100,2,100),100),AND_entre_valores(valores_acotados_ventana_3U100,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_100,2,100),100),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_155,2,155),155),AND_entre_valores(valores_acotados_ventana_2U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_155,2,155),155),AND_entre_valores(valores_acotados_ventana_3U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_155,2,155),155),AND_entre_valores(valores_acotados_ventana_4U155,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_4U_155,3,155),155),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_197,3,197),197),AND_entre_valores(valores_acotados_ventana_2U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_197,3,197),197),AND_entre_valores(valores_acotados_ventana_3U197,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_3U_197,3,197),197),
                                                                                                                                                                         AND_entre_valores(valores_acotados_ventana_1U350,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_350,1,350),350),
                                                                                                                                                                         AND_entre_valores(valores_para_acotar_la_ventana_1U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_1U_400,1,400),400),AND_entre_valores(valores_para_acotar_la_ventana_2U400,funcion_de_mantenimiento(tiempo_establ_por_IEEE_mantenimiento_2U_400,1,400),400))]
    return resultado_suma
