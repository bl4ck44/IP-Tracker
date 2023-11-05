import request
import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

os.system("clear")

print("")

print("\033[34m ._____________        ___________                     __                  \033[0m")
print("\033[34m |   \______   \       \__    ___/___________    ____ |  | __ ___________  \033[0m")
print("\033[34m |   ||     ___/  ______ |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ \033[0m")
print("\033[34m |   ||    |     /_____/ |    |   |  | \// __ \\  \___|    <\  ___/|  | \/ \033[0m")
print("\033[34m |___||____|             |____|   |__|  (____  /\___  >__|_ \\___  >__|    \033[0m")
print("\033[34m                                             \/     \/     \/    \/        \033[0m")


def menu_principal():
	while True:
		print("\n[1] Obtener geolocalizacion de una IP")
		print("[2] Obtener informacion del número de teléfono")
		print("[3] Salir")
		opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
		if opcion == "":
			print("\033[1m\n[+] Por favor ingrese una opción: \033[0m")
		elif opcion == "1":
			menu1()
		elif opcion == "2":
			menu2()
		elif opcion == "3":
			break


def menu1():
	while True:
		print("\n[1] Método 1")
		print("[2] Método 2")
		print("[99] Volver al menu")
		opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
		if opcion == "":
			print("\033[1m\n[+] Por favor ingrese una opción: \033[0m")
		elif opcion == "1":
			ip_address = input("\033[1m\nIngrese la Dirección IP: \033[0m") # Dirección IP de ejemplo
			url = f'http://ip-api.com/json/{ip_address}'
			response = requests.get(url)
			if response.status_code == 200:
				data = response.json()
				country = data["country"]
				city = data["city"]
				lat = data["lat"]
				lon = data["lon"]
				with open("IP.txt", "w+") as file:
					file.write(f'Pais: {country}\n')
					file.write(f'Ciudad: {city}\n')
					file.write(f'Latitud: {lat}\n')
					file.write(f'Longitud: {lon}\n')
				
			print(f'\nPaís: {country}')
			print(f'Ciudad: {city}')
			print(f'Latitud: {lat}')
			print(f'Longitud: {lon}\n')
				
		elif opcion == "2":
			def ip_info(ip_address):
				url = f"https://ipinfo.io/{ip_address}/json"
				response = requests.get(url)
				if response.status_code == 200:
					data = response.json()
					ip = data["ip"]
					hostname = data["hostname"]
					city = data["city"]
					region = data["region"]
					country = data["country"]
					postal = data["postal"]
					latitude = data["loc"]
					longitude = data["loc"]
					with open("IP2.txt", "w+") as file:
						file.write(f'IP address: {ip}\n')
						file.write(f'Hostname: {hostname}\n')
						file.write(f'City: {city}\n')
						file.write(f'Region: {region}\n')
						file.write(f'Country: {country}\n')
						file.write(f'Postal code: {postal}\n')
						file.write(f'Latitude: {latitude}\n')
						file.write(f'Longitude: {longitude}\n')
				data = response.json()
				print(f"IP address: {data['ip']}")
				print(f"Hostname: {data['hostname']}")
				print(f"City: {data['city']}")
				print(f"Region: {data['region']}")
				print(f"Country: {data['country']}")
				print(f"Postal code: {data['postal']}")
				print(f"Latitude: {data['loc'].split(',')[0]}")
				print(f"Longitude: {data['loc'].split(',')[1]}")
			ip_address = input("\033[1m\nEnter an IP address: \033[0m")
			ip_info(ip_address)
			
		elif opcion == "99":
			menu_principal()
			


def menu2():
	while True:
		country = input("País (sin +): ")
		number = input("Número: ")
		print("")
		victim_number = '+' + country + number
		# Crear un objeto PhoneNumber con el número de teléfono
		phone_number = phonenumbers.parse(victim_number)
		# Guardar la salida en un archivo llamado "número.txt"
		with open("número.txt", "w") as f:
			f.write("Numero valido: {}\n".format(phonenumbers.is_valid_number(phone_number)))
			f.write("Numero posible: {}\n".format(phonenumbers.is_possible_number(phone_number)))
			f.write("Numero: {}\n".format(phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)))
			f.write("Geolocalizacion: {}\n".format(phonenumbers.geocoder.description_for_number(phone_number, "en")))
			f.write("Operador: {}\n".format(phonenumbers.carrier.name_for_number(phone_number, "ec")))
	
		print("Numero valido: {}".format(phonenumbers.is_valid_number(phone_number)))
		print("Numero posible: {}".format(phonenumbers.is_possible_number(phone_number)))
		print("Numero: {}".format(phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)))
		print("Geolocalizacion: {}".format(phonenumbers.geocoder.description_for_number(phone_number, "en")))
		print("Operador: {}".format(phonenumbers.carrier.name_for_number(phone_number, "ec")))
		print("")


menu_principal()