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
		return False
def escoger():
	print("\n\n1.-Consulta\n2.-Registro\n3.-Salir")
	respuesta = int(raw_input("Opcion: "))
	if respuesta == 1:
		return 1
	elif respuesta == 2:
		return 2
	elif respuesta == 3:
		return 3
	else:
		escoger()


def registro(Origen,Destino):
	try:
		tiempo = 60 * 15
		for i in range(1,48):
			archivo = open("registroTiempos.txt","a")
			print("Ida: ")
			tiempoTraslado = googleAPI.obtenerTiempo(Origen,Destino)
			archivo.write("Ida:\n")
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)

			print("Regreso: ")
			tiempoTraslado = googleAPI.obtenerTiempo(Destino,Origen)
			archivo.write("Regreso:\n")
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)
			archivo.close()
			time.sleep(tiempo)
	except KeyboardInterrupt:
		print("Proceso Interrumpido")
	except:
		print("Algo salió mal")

def consulta(Origen,Destino):
	try:
		archivo = open("registroTiempos.txt","a")
		print("Ida: ")
		tiempoTraslado = googleAPI.obtenerTiempo(Origen,Destino)
		archivo.write("Ida:\n")
		registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
		archivo.write(registro)
		print("Regreso: ")
		tiempoTraslado = googleAPI.obtenerTiempo(Destino,Origen)
		archivo.write("Regreso:\n")
		registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
		archivo.write(registro)
		archivo.close()		
	except KeyboardInterrupt:
		print("Proceso interrumpido")
	except:
		print("Algo Salio Mal")

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
	respuesta = responder()
	if respuesta == False:
		entrada()
	dia = time.strftime("%d/%m/%y")
	nombreArchivo = "registro" + dia

	archivo = open("registroTiempos.txt" + ".txt","w")
	archivo.write("\n" + dia)
	archivo.write("\nOrigen: " + RegOrigen + "\nDestino: " + RegDestino + "\n\n")
	archivo.close()
	respuesta = escoger()
	if respuesta == 1:
		consulta(Origen,Destino)
	elif respuesta == 2:
		registro(Origen,Destino)
	else:
		print("Auf Wiedersehen")

entrada()