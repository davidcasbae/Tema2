import threading
import time

def procesar_usuario(id, nombre, edad):
    time.sleep(1)
    print(f"Id: {id} ,Nombre: {nombre}, Edad: {edad}")

usuarios = [
    (1, {'nombre': 'Ana', 'edad': 28}),
    (2, {'nombre': 'Lorenzo', 'edad': 34}),
    (3, {'nombre': 'Salma', 'edad': 23}),
    (4, {'nombre': 'Pedro', 'edad': 40}),
    (5, {'nombre': 'Luisa', 'edad': 19}),
]
hilos = []
for usuario in usuarios:
    id, info = usuario
    hilo = threading.Thread(target=procesar_usuario, args=(id,), kwargs= info)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("ha finalizado")