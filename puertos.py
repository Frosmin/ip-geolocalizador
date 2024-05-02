import socket

def escanear_puertos(ip):
    puertos_abiertos = []
    for puerto in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            puertos_abiertos.append(puerto)
        sock.close()
    return puertos_abiertos

ip = '0.0.0.0'  #ip
puertos_abiertos = escanear_puertos(ip)

print(f'Puertos abiertos en {ip}: {puertos_abiertos}')