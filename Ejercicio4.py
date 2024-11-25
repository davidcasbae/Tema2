import threading

contador = 1
ciclos = 5
lock = threading.Lock()
cond = threading.Condition()

def preparacion(cond):
    global contador
    for i in range(1, ciclos + 1):
        with cond:
            cond.wait_for(lambda: contador == 1)
            print(f"Preparacion {i} completada")
            contador = 2
            cond.notify_all()

def procesamiento(cond):
    global contador
    for i in range(1, ciclos + 1):
        with cond:
            cond.wait_for(lambda: contador == 2)
            print(f"procesamiento {i} completado")
            contador = 3
            cond.notify_all()

def empaque(cond):
    global contador
    for i in range(1, ciclos + 1):
        with cond:
            cond.wait_for(lambda: contador == 3)
            print(f"empaque {i} completado")
            contador = 1
            cond.notify_all()

hilo1 = threading.Thread(target=preparacion, args=(cond,))
hilo2 = threading.Thread(target=procesamiento, args=(cond,))
hilo3 = threading.Thread(target=empaque, args=(cond,))

hilo1.start()
hilo2.start()
hilo3.start()

with cond:
    cond.notify()

hilo1.join()
hilo2.join()
hilo3.join()