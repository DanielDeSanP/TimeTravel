# -*- coding:utf-8 -*-
import googleAPI
import time
from osName import clear
import colorText

colores = colorText.bcolors()

# googleAPI -> métodos para conectarse a la API de google
# time -> Obtener el tiempo 
# osName -> Detecta el sistema operativo y nos regresa una 
# 			funcion lambda que ejecuta un clear o cls en 
# 			consola 


"""
	Programa diseñado para hacer un registro
	estadístico de tiempos de traslado de un punto a otro.
	Usa una API de Google para obtener esos datos.
	El programa llama a la API por medio de un solicitud
	HTTPS cada media hora durante las 24 de un día.

	Donde inicia la ejecuacion en este modulo es en pedirDireccion. 
	

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
	Funcion: desplegar menu 1
	Entrada: void
	Salida: entero
	Proceso:
		Despliega un menu para el usuario, donde podrá 
		escoger si solo requiere hacer una consulta o un registro.
		Se hace por medio de if elif, cada opcion regresa un numero
		bandera que servirá en la funcion entrada.

"""
def desplegarMenu1():
	try:
		clear()
		print("\n\n1.-Consulta\n2.-Registro\n3.-Salir")
		respuesta = int(raw_input("Opcion: "))
		if respuesta == 1:
			return 1
		elif respuesta == 2:
			return 2
		elif respuesta == 3:
			return 3
		else:
			desplegarMenu1()
	except ValueError:
		# En caso de que se introduzca un dato no admitido
		print("ERROR Tipo de valor no admitido")
		desplegarMenu1()
"""
	Funcion: desplegar menu 2
	Entrada: void 
	Salida: entero
	Proceso:
		Hace lo mismo que la funcion desplegar menu 1, solo que
		este despliega un menu, con una opcion más, para cuando
		se haya realizado una vez el proceso. 

"""

def desplegarMenu2():
	try:
		clear()
		print("\n\n1.-Consulta\n2.-Registro\n3.-Introducir Nuevas direcciones\n4.-Salir")
		respuesta = int(raw_input("Opcion: "))
		if respuesta == 1:
			return 1
		elif respuesta == 2:
			return 2
		elif respuesta == 3:
			return 3
		elif respuesta == 4:
			return 4
		else:
			desplegarMenu2()
	except ValueError:
		# En caso de que se introduzca un dato no admitido
		print("ERROR Tipo de valor no admitido")
		desplegarMenu2()	
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
		# Establece el intervalo de tiempo en el que se va a registrar datos.
		# 60 segundos por 30 equivale a media hora
		# Cada media hora se va a hacer un registro.
		tiempo = 60 * 30
		for i in range(1,48):
			# Abrimos archivo de registros
			archivo = open("registroTiempos.txt","a")
			print("Ida: ")
			# llamamos a la funcion obtenerTiempo del modulo googleAPI
			tiempoTraslado = googleAPI.obtenerTiempo(Origen,Destino)
			# Escribimos los datos recibidos
			archivo.write("Ida:\n")
			# Escribimos la hora en el que se hizo el registro
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)
			# Hacemos el mismo proceso, pero esta vez para el tiempo de regreso
			# Al llama obtenerTiempo invertimos el orden de entrada
			print("Regreso: ")
			tiempoTraslado = googleAPI.obtenerTiempo(Destino,Origen)
			archivo.write("Regreso:\n")
			registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
			archivo.write(registro)
			# Cerramos el archivo
			archivo.close()
			# Ponemos el programa a dormir, el tiempo definido
			time.sleep(tiempo)
	except KeyError:
		# En caso de que no se extraiga bien el dato del json 
		print("No se pudo obtener los datos")
	except KeyboardInterrupt:
		# En caso de que se interrumpa la ejecucion por teclado
		print("Proceso Interrumpido")
	except:
		# Para cualquiere otro posible error que aparezca.
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
		print("Ida: ")
		# Llamamos a obtenerTiempo en googleAPI
		tiempoTraslado = googleAPI.obtenerTiempo(Origen,Destino)
		registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
		print(colores.OKBLUE + "Regreso: " + colores.ENDC)
		# Hacemos lo mismo para obtener el tiempo de regreso, invirtiendo las entradas
		# en obtenerTiempo
		print("Regreso: ")
		tiempoTraslado = googleAPI.obtenerTiempo(Destino,Origen)
		registro = time.strftime("%l : %M %p") + "----> " + tiempoTraslado + "\n"
	except KeyboardInterrupt:
		# En caso de que se mate al programa con teclado
		print("Proceso interrumpido")
	except KeyError:
		# En caso de que no se hayan extraido correctamente los datos.
		print("No se pudo obtener los datos")
	except:
		# En caso de que otro error ocurra
		print("Algo Salio Mal")
"""
	Funcion: pedir direccion
	Entrada: void
	Salida: void
	Proceso:
		La funcion se encarga de pedir al usuario las referencias del origen y el destino.
		Hace un formato a la cadena para concatenar con un url para hacer la peticion de tiempo
		HTTPS.

"""
def pedirDireccion():
	clear()
	Origen = ""
	Destino = ""
	firstExecution = True
	entrada = raw_input("Origen: ")
	RegOrigen = entrada

	# Recibimos las cadenas de origen y destino, y le damos formato
	# Para enviarla a la API de google.
	# Se separa la cadena en arreglo con cada espacio detectado
	palabrasSepa = entrada.split(" ")

	# Concatenamos cada elemento del arreglo para forma una cadena sin espacios.
	for palabra in palabrasSepa:
		Origen += palabra

	# Hacemos lo mismo para la cadena recibida en destino
	entrada = raw_input("Destino: ")
	RegDestino = entrada
	palabrasSepa = entrada.split(" ")

	for palabra in palabrasSepa:
		Destino += palabra
	# Vemos de que no sean cadenas vacías, si lo son, ejecutamos de nuevo la función
	if RegOrigen == "" or RegDestino == "":
		pedirDireccion()
	# LLamamos a la funcion ejecutar.
	ejecutar(Origen,Destino,RegOrigen,RegDestino,firstExecution)
"""
	Funcion: ejecutar
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
def ejecutar(Origen,Destino,RegOrigen,RegDestino,firstExecution):
	try:
		if firstExecution == True:
			# Cuando se ejecuta el menu por primera vez
			# Pedimos las direcciones a la API de Google
			googleAPI.obtenerDirecciones(Origen,Destino)
			# Llamamos a la función responder que devuelve un booleano
			respuesta = responder()
			if respuesta == False:
				# Si la respuesta del usuario es negativa, se vuelve a pedir la direccion
				pedirDireccion()
			respuesta = desplegarMenu1()
		else:
			# Cuando se ejecuta el menu por segunda vez, se despliega el menu con una opcion mas
			respuesta = desplegarMenu2()

		if respuesta == 1:
			# Opcion 1
			# Consulta simple 
			# Se llama a la función consulta
			consulta(Origen,Destino)
			# Cambiamos la bandera de primera ejecucion
			firstExecution = False
			# Recibimos un caracter para confirmar fin de la tarea
			enter = raw_input("Presione enter...")
			# Llamamos a la funcion ejecutar nuevamente
			ejecutar(Origen,Destino,RegOrigen,RegDestino,firstExecution)
		elif respuesta == 2:
			# Opcion 2
			# Consulta con registro
			# Obtenemos la fecha 
			dia = time.strftime("%d/%m/%y")
			nombreArchivo = "registro" + dia
			archivo = open("registroTiempos.txt","a")
			archivo.write("\n" + dia)
			archivo.write("\nOrigen: " + RegOrigen + "\nDestino: " + RegDestino + "\n\n")
			# Concatenamos
			nombreArchivo = "registro" + dia
			# Escribimos en el archivo el día, el destino y el origen.
			archivo.write("\n" + dia)
			archivo.write("\nOrigen: " + RegOrigen + "\nDestino: " + RegDestino + "\n\n")
			# Cerramos el archivo
			archivo.close()
			# Llamamos a la funcion registro
			registro(Origen,Destino)
			# Cambiamos la bandera de primera ejecucion
			firstExecution = False
			# Esperamos respuesta de confirmación del usuario
			enter = raw_input("Presione enter...")
			# Llamamos la funcion ejecutar.
			ejecutar(Origen,Destino,RegOrigen,RegDestino,firstExecution)
		elif respuesta == 3 and firstExecution == False:
			# Opcion 3:
			# Cambiar de direcciones escritas.
			pedirDireccion()
		else:
			# Cualquier otra opción, salir del programa. 
			print("¡Adiós!")
			# Cerramos el interprete de Python 
			quit()
	except KeyError:
		# Error al extraer los datos del json recibido del HTTP request en el módulo googleAPI
		print("Error al obtener los datos")
	except KeyboardInterrupt:
		# Excepcion para cuando se ordena desde teclado el cierre del programa. 
		print("Proceso interrumpido")
