import threading
import time
from random import randint

senal = threading.Event()

def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posición, esperando señal de salida")
    senal.wait()
    print(f"Corredor {id_corredor} comienza a correr")
    time.sleep(randint(1,3))
    print(f"Corredor {id_corredor} ha llegado a la meta!!")

def iniciar_carrera():
        print("Señal de salida en dos segundos...")
        time.sleep(2)
        print("Salida!!")
        senal.set()

corredores = []
for i in range(5):
    c = threading.Thread(target=corredor, args=(i+1,))
    corredores.append(c)
    c.start()

inicio_senal = threading.Thread(target=iniciar_carrera)
inicio_senal.start()

for c in corredores:
    c.join()
    inicio_senal.join()

print("Todos los corredores han llegado a la meta")