import requests
import webbrowser

def geolocalizar_ip(ip):
    respuesta = requests.get(f'http://ip-api.com/json/{ip}')
    datos = respuesta.json()

    return datos

ip = '0.0.0.0'  #ip que quieres buscar
datos = geolocalizar_ip(ip)

print(f'IP: {datos["query"]}')
print(f'Ciudad: {datos["city"]}')
print(f'Región: {datos["regionName"]}')
print(f'País: {datos["country"]}')
print(f'ISP: {datos["isp"]}')


latitud = datos['lat']
longitud = datos['lon']


url = f'https://www.google.com/maps/?q={latitud},{longitud}'

webbrowser.open(url)