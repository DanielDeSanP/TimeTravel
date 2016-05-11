# -*- coding:utf-8 -*-
import urllib, json
from pprint import pprint

"""
	Funcion: obtenerDirecciones
	Entrada: str origen, str destino
	Salida: void
	Proceso:

		Recibe dos cadenas con las referencias a los lugares, que se van 
		a concatenar con el url, para hacer la peticion HTTPS. La Respuesta
		recae en response, y los datos del json caen en data, luego 
		la cadena relacionada a origin_addresses es asignada a lista 
		(que es una lista) para luego ser imprimida en consola. Si la cadena
		está vacia, significa que la API no captó la referencia al lugar 
		y por lo tanto regresa un json con error. Por ello se hace una comparación,
		y si se da una cadena vacia se levanta la excepcion KeyError que se recibe 
		en TimeTraveler. Se imprime tanto la direccion devuelta por la API del origen
		como del destino.

"""
def obtenerDirecciones(origen,destino):
	# Concatenamos la cadena con el url, para llamar la api de google. 
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origen + "|&destinations=" + destino + "&mode=driving&language=fr-SP"
	# Obtenemos la respuesta en response
	response = urllib.urlopen(url)
	# Cargamos el json
	data = json.load(response)
	# Obtenemos la direccion del origen
	lista = data['origin_addresses']
	print ("\n")
	# Se compara si la cadena está vacia.
	if lista[0] == "":
		raise KeyError
	# Si la cadena no está vacia se despliega en pantalla
	print lista[0]
	# Obtenemos la direccion del destino
	lista = data['destination_addresses']
	# Comprobamos si no está vacia.
	if lista[0] == "":
		raise KeyError
	print("\n")
	# Imprimimos la informacion 
	print lista[0]
	print ("\n")


"""
	Funcion: obtenerTiempo
	Entrada: str origen, str destino
	Salida: str 
	Proceso:

		Las dos cadenas de entrada se concatenan con el url, para hacer la petición 
		HTTPS, la respuesta la recibe response, y se carga el json en data. Ya obtenidos los 
		datos accedemos al tiempo del json y lo retornamos. Los posibles errores son falla en
		la clave del diccionario, en dado caso de que el json recibido sea erroneo. Todas las
		execpciones retornan la cadena ERROR que se expresa tanto en consola como en el archivo
		registro. 

"""
def obtenerTiempo(origen,destino):
	try:
	# Concatenamos la cadena con el url, para llamar la api de google. 
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origen + "|&destinations=" + destino + "&mode=driving&language=fr-SP"
		# url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=19.3022924,-99.11184889999998|&destinations=paseoacoxpa&mode=driving&language=fr-SP"
		response = urllib.urlopen(url)
		# Obtenemos el json
		print("Logramos conectarnos con la API")
		# Cargamos el json
		data = json.load(response)
		print("Obtuvimos los datos...")
		# Imprimimos el tiempo
		print data['rows'][0]['elements'][0]['duration']['text']
		# Retornamos el tiempo en forma de cadena.
		return data['rows'][0]['elements'][0]['duration']['text']
	except IOError:
		print("Error con la conexión")
		return "ERROR"
	except KeyError:
		print("No se pudo obtener los datos")
		return "ERROR"
	except:
		print("No se puede conectar a internet")
		return "ERROR"
	finally:
		print("Espere...")