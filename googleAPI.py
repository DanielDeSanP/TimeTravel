import urllib, json
def obtenerTiempo(origen,destino):
	try:
	# Concatenamos la cadena con el url, para llamar la api de google. 
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + Origen + "|&destinations=" + Destino + "&mode=driving&language=fr-SP"
		# url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=19.3022924,-99.11184889999998|&destinations=paseoacoxpa&mode=driving&language=fr-SP"
		response = urllib.urlopen(url)
		# Obtenemos el json
		data = json.loads(response.read())

		archivo = open("ElYeison.txt",w)
		archivo2 = open("Respuesta.json",w)

		archivo.write(data)
		archivo.close()
		print data
	except:
		print("No se puede conectar a internet")
	finally:
		print("Proceso terminado")