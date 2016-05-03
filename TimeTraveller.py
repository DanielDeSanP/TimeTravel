# -*- coding:utf-8 -*-
import googleAPI
import time
"""
	Programa diseñado para hacer un registro
	estadístico de tiempos de traslado de un punto a otro.
	Usa una API de Google para obtener esos datos.
	El programa llama a la API por medio de un solicitud
	HTTPS cada media hora durante las 24 de un día.
	

"""
entrada = raw_input("Origen: ")
palabrasSepa = entrada.split(" ")
Origen = ""
Destino = ""
for palabra in palabrasSepa:
	Origen += palabra

entrada = raw_input("Destino: ")
palabrasSepa = entrada.split(" ")
for palabra in palabrasSepa:
	Destino += palabra
print (Origen)
print (Destino)

tiempo = 60 * 30

try:
	for i in range(1,48):
		archivo = open("registroTiempos.txt","a")
		googleAPI.obtenerTiempo(Origen,Destino)
		archivo.write("a\n")
		archivo.close()
		time.sleep(tiempo)

except KeyboardInterrupt:
	print("Proceso interrumpido")
except:
	print("Algo salio mal")