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
def responder():
	print("Son las direcciones correctas? S/N")
	respuesta = raw_input("Respuesta: ")
	if respuesta == 's' or respuesta == 'S':
		return True
	elif respuesta == "n" or respuesta == 'N':
		return False
	else:
		print("Respuesta no valida")
		responder()

def entrada():
	entrada = raw_input("Origen: ")
	RegOrigen = entrada
	palabrasSepa = entrada.split(" ")
	Origen = ""
	Destino = ""
	for palabra in palabrasSepa:
		Origen += palabra
	entrada = raw_input("Destino: ")
	RegDestino = entrada
	palabrasSepa = entrada.split(" ")
	for palabra in palabrasSepa:
		Destino += palabra
	googleAPI.obtenerDirecciones(Origen,Destino)
	# respuesta = responder()
	# if respuesta == False:
	# 	entrada()
	tiempo = 60 * 15
	archivo = open("registroTiempos.txt","a")
	dia = time.strftime("\n%d/%m/%y")
	archivo.write(dia)
	archivo.write("\nOrigen: " + RegOrigen + "\nDestino: " + RegDestino + "\n\n")
	archivo.close()
	try:
		for i in range(1,48):
			archivo = open("registroTiempos.txt","a")
			tiempoTraslado = googleAPI.obtenerTiempo(Origen,Destino)
			archivo.write("Ida:\n")
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)
			tiempoTraslado = googleAPI.obtenerTiempo(Destino,Origen)
			archivo.write("Regreso:\n")
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)
			archivo.close()
			# time.sleep(tiempo)

	except KeyboardInterrupt:
		print("Proceso interrumpido")
	except:
		print("Algo salio mal")
entrada()