import threading
import time


class SesionUsuario:
    def iniciar_sesion(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def mostrar_sesion(self):
        print(f'{self.nombre_usuario}')

def main():
        datos_sesion = threading.local()

        def gestionar_sesion(nombre_usuario):
            datos_sesion.sesion_usuario = SesionUsuario()
            datos_sesion.sesion_usuario.iniciar_sesion(nombre_usuario)
            time.sleep(2)
            datos_sesion.sesion_usuario.mostrar_sesion()

        hilos = []
        nombres_usuarios = ["Alicia", "Ana", "Manuel", "Hugo"]

        for nombre in nombres_usuarios:
            hilo = threading.Thread(target=gestionar_sesion(nombre))
            hilos.append(hilo)
            hilo.start()

        for hilo in hilos:
            hilo.join()

        print("Todas las sesiones han sido gestionadas correctamente.")
