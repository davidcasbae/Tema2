import threading
import time


class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombreArchivo, numeroLineas):

        super().__init__()
        self.nombreArchivo = nombreArchivo
        self.numeroLineas = numeroLineas

    def run(self):
        print(f"{self.nombreArchivo} - Línea {self.numeroLineas}")
        time.sleep(2)

        archivo1 = ("\n\n\n")
        archivo2 = ("\n\n")
        archivo3 = ("\n\n\n")

        nombres = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

        hilos = []
        for i in range(3):
            hilo = ProcesadorArchivo(nombreArchivo= nombres, numeroLineas= 1)
            hilos.append(hilo)
            hilo.start()

        for hilo in hilos:
            hilo.join()

        print("Todos los archivos han sido procesados")