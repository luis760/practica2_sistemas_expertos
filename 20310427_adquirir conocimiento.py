# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:53:02 2023

@author: 52331
"""
import numpy as np
import os
import mysql.connector
opc=1
while opc!=0:

# Conectar a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="prueba"
        )

    cursor = conn.cursor()  
    print("--------------------seleccione la opcion que desea--------------------------------------")
    print("Digite la pregunta que desea ejecutar o de lo contrario seleccione la opcion 1 o 2 ")
    print("1-Meter un dato nuevo")
    print("2-ver todos los datos de la BD")
    dato = input("")
    if dato!='1' and dato !='2':
            dato== dato;
            cursor.execute("SELECT * FROM `datos` WHERE pregunta='" + dato + "';")
            
            resultados = cursor.fetchall()
            
            for fila in resultados:
                print(f"\n respuesta: {fila[1]}")
                
                conn.close()
    else :
                    if dato=='1' :
                        pregunta = input("Digite la pregunta que desea agregar\n")
                        respuesta = input("\nDigite la respuesta a la pregunta\n")
                        sql_insert = "INSERT INTO `datos` (`pregunta`, `respuesta`, `id`) VALUES (%s, %s, NULL)"
                        valores = (pregunta, respuesta)
                        cursor.execute(sql_insert, valores)
                        conn.commit()
                        print("datos guardados con exito")
                        conn.close()
                    elif dato=='2' :
                            cursor.execute("SELECT * FROM `datos` WHERE 1")
                            resultados = cursor.fetchall()
                            for fila in resultados:
                                print(f"\nID: {fila[2]},\n pregunta: {fila[0]},\n respuesta: {fila[1]}")
                                conn.close()
    opc2=input("Presione cualquier numero diferente de 0 para continuar ")
    opc=int(opc2)
  
    
                                
                                    