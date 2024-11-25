import threading
import time


semaforo = threading.Semaphore(3)

def acceder_estacionamiento(id_vehiculo):
    semaforo.acquire()
    print(f"Vehículo {id_vehiculo} ha entrado al estacionamiento")
    import random
    time.sleep(random.uniform(1, 3))
    print(f"Vehículo {id_vehiculo} ha salido del estacionamiento")
    semaforo.release()

vehiculos = []
for i in range(10):
    vehiculo = threading.Thread(target=acceder_estacionamiento, args=(i,))
    vehiculos.append(vehiculo)
    vehiculo.start()

for vehiculo in vehiculos:
    vehiculo.join()