# -*- coding:utf-8 -*-
import urllib, json
from pprint import pprint
def obtenerDirecciones(origen,destino):
	# try: 
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origen + "|&destinations=" + destino + "&mode=driving&language=fr-SP"
	response = urllib.urlopen(url)
	data = json.load(response)
	lista = data['origin_addresses']
	print ("\n")
	if lista[0] == "":
		raise KeyError
	print lista[0]
	lista = data['destination_addresses']
	if lista[0] == "":
		raise KeyError
	print("\n")
	print lista[0]
	print ("\n")
	# except KeyError:
	print("No se pudo obtener los datos")
	# except:
	print("Algo salió mal")

def obtenerTiempo(origen,destino):
	try:
	# Concatenamos la cadena con el url, para llamar la api de google. 
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origen + "|&destinations=" + destino + "&mode=driving&language=fr-SP"
		# url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=19.3022924,-99.11184889999998|&destinations=paseoacoxpa&mode=driving&language=fr-SP"
		response = urllib.urlopen(url)
		# Obtenemos el json
		print("Logramos conectarnos con la API")
		data = json.load(response)
		print("Obtuvimos los datos...")

		# archivo = open("ElYeison.txt","w")
		# archivo2 = open("Respuesta.json","w")
		
		# archivo.write(data)
		# archivo.close()
		# archivo2.close()
		print data['rows'][0]['elements'][0]['duration']['text']
		return data['rows'][0]['elements'][0]['duration']['text']
	except IOError:
		print("Error con la conexión")
	except KeyError:
		print("No se pudo obtener los datos")
	except:
		print("No se puede conectar a internet")
		return "ERROR"
	finally:
		print("Espere...")