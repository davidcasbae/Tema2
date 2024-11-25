import threading
import time


nombre= threading.local()
class SesionUsuario:
    def iniciar_sesion(self, nombre_usuario):
        nombre.nombre_usuario = nombre_usuario
    def mostrar_sesion(self):
        print(f"Sesión iniciada para el usuario: {nombre.nombre_usuario}")
    def gestionar_sesion(self, nombre_usuario):
        self.iniciar_sesion(nombre_usuario)
        time.sleep(2)
        self.mostrar_sesion()

def main():
    hilos = []
    nombres_usuarios = ["Alicia", "Ana", "Manuel", "Hugo"]

    for nombre_usuario in nombres_usuarios:
        sesion = SesionUsuario()
        hilo = threading.Thread(target=sesion.gestionar_sesion, args=(nombre_usuario,))
        hilos.append(hilo)
        hilo.start()

        for hilo in hilos:
            hilo.join()

    print("Todas las sesiones han sido gestionadas correctamente.")
if __name__ == '__main__':
    main()