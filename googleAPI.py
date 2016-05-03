# -*- coding:utf-8 -*-
import urllib, json
from pprint import pprint
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
	except:
		print("No se puede conectar a internet")
	finally:
		print("Proceso terminado")