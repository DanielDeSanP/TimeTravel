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

"""
	Funcion: responder
	Entrada: void 
	Salida: boleano
	Proceso:
		Pregunta al usuario si las direcciones introducidas son correctas.
		Por medio de if elif, se hace la eleccion, se devuelve true o false.

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

"""
	Funcion: escoger
	Entrada: void
	Salida: entero
	Proceso:
		Despliega un menu para el usuario, donde podrá 
		escoger si solo requiere hacer una consulta o un registro.
		Se hace por medio de if elif, cada opcion regresa un numero
		bandera que servirá en la funcion entrada.

"""
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
"""
	Funcion: registro
	Entrada: str Origen, str Destino
	Salida: void 
	Proceso:

		Primero se abre el archivo de registros, y luego
		se llama al metodo obtenerTiempo pasando Origen y Destino
		como parametros de entrada, del módulo googleAPI. Se 
		escribe con formato en el archivo, y se despliega en consola.
		Se realiza dos veces, una para obtener ida y otra para obtener
		regreso. Todo el proceso está contenido en un ciclo for 
		que se repite en total 48 veces, al final de cada iteración
		se espera el programa media hora (60*30),de este modo 
		se hace un registro cada media hora un día entero. 

"""

def registro(Origen,Destino):
	try:
		tiempo = 60 * 30
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
	except KeyError:
		print("No se pudo obtener los datos")
	except KeyboardInterrupt:
		print("Proceso Interrumpido")
	except:
		print("Algo salió mal")


"""
	Funcion: consulta
	Entrada: str Origen, str Destino
	Salida: void 
	Proceso:

		Se abre el archivo de registros, y luego se hace el llamado
		al metodo obtenerTiempo, con parámetros de entrada
		Origen Destino, del módulo googleAPI, que devuelve 
		una cadena con el tiempo de traslado, se escribe con formato
		en el archivo, y la informacion obtenida se despliega en consola.

		Se realiza dos veces, una para obtener tiempo de ida y otra tiempo de regreso,
		para el segundo caso solo se envian las cadenas Origen Destino invertidas.

"""
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
	except KeyError:
		print("No se pudo obtener los datos")
	except:
		print("Algo Salio Mal")
"""
	Funcion: entrada
	Entrada: void
	Salida: void 
	Proceso:

		Se pide origen y destino al usuario, se le da formato a las
		cadenas para evitar posibles problemas con el llamado HTTPS.
		Luego se llama al metodo obtenerDirecciones con parametros de entrada
		Origen Destino, para obtener las direcciones registradas en la API.
		Se despliegan dichas direcciones en pantalla y luego se llama al metodo 
		responder para preguntar al usuario si las direcciones son correctas.
		Una vez realizado ello, se abre el archivo de registros para anotar
		las direcciones, la hora y la fecha. Luego se llama a la funcion escoger 
		para desplegar un menu al usuario, donde escogerá si quiere hacer
		una consulta o un registro, dependiendo de que se escoja el metodo 
		devolverá un numero que lo captará un if elif, que llamará la funcion 
		escogida, enviando como parametros de entrada Origen y Destino. 

"""

def entrada():
	try:
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
			o = entrada()
		else:

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
	except KeyError:
		print("Error al obtener los datos")
	finally:
		print("Proceso terminado")
