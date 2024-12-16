import threading
import queue
import time
import random

numero = 1
cola = queue.Queue(maxsize=5)

def cliente(id_cliente):
    global numero
    while True:
        cola.put(numero)
        print(f"Cliente {id_cliente}: Generó pedido-{numero}")
        time.sleep(random.uniform(1, 2))

def empleado(id_empleado):
    global numero
    while True:
        numero = cola.get()
        print(f"Empleado {id_empleado}: Procesó pedido-{numero}")
        time.sleep(random.uniform(2, 3))
        cola.task_done()

        if numero > 15 and cola.empty():
            break

hilo_cliente = threading.Thread(target=cliente, daemon=True)
hilo_empleado = threading.Thread(target=empleado, daemon=True)

hilo_cliente.start()
hilo_empleado.start()
