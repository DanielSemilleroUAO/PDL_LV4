# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:21:21 2018

@author: Daniel Delgado Rodrìguez
         Juan Fernando Guerrero F.  
"""
###############################################################################
###############################################################################
        #########           ###########                ###########            
        #        #      @        #                          # 
        #        #               #                          #
        #        #      #        #         #########        #
        #########       #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #########       #   ###########    #########        #
###############################################################################
###############################################################################

import paho.mqtt.client as mqtt
#-------------------FUNCIONES MQTT---------------------------------------------
def leer_valores(archivo):
    f = open(archivo)
    linea = f.readline()
    f.close()
    return linea
def guardar_valores(archivo,mensaje):
    f = open(archivo,'w+')
    f.write(mensaje)
    f.close()   
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([("contenedor/panel",2),("contenedor/azul",2),("contenedor/verde",1),("contenedor/gris",0)])
def on_message(client, userdata, msg):
    dato_c = msg.payload.decode()
    dato = dato_c.split(",")
    print(dato)        
    if dato[0] == 'A':
        guardar_valores("MEDIDA_CONTENEDORES/CA.txt",dato[1])
        print("Caneca Azul")
    if dato[0] == 'V':
        guardar_valores("MEDIDA_CONTENEDORES/CV.txt",dato[1])
        print("Caneca Verde")
    if dato[0] == 'G':
        guardar_valores("MEDIDA_CONTENEDORES/CG.txt",dato[1])
        print("Caneca Gris")
    if dato[0] == "Hello world!":
        print("Yes!")
        client.disconnect()
    if dato[2] == '3':
        print(leer_valores("MEDIDA_CONTENEDORES/U.txt"))
        print(leer_valores("MEDIDA_CONTENEDORES/CA.txt"))
        print(leer_valores("MEDIDA_CONTENEDORES/CV.txt"))
        print(leer_valores("MEDIDA_CONTENEDORES/CG.txt"))
        #envio_App.conexion_APP_WEB(ID,ContenedorAzul,ContenedorVerde,ContenedorGris,0,0)
#----------------INICIO PROGRAMA-----------------------------------------------
client = mqtt.Client()
client.connect("192.168.4.1",1883,2)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
