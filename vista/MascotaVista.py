from controlador.MascotaControlador import MascotaControlador
from modelo.MascotaModelo import MascotaModelo

import os

class MascotaVista:

    def __init__(self):
        # Inicializar controlador y modelo de mascotas
        self.__mascota_controlador = MascotaControlador(self)
        self.__mascota_modelo = MascotaModelo()
        self.mostrar_menu()

    def mostrar_menu(self):
        # Mostrar el menú de opciones
        print("\n--- Menú ---")
        print("1. Listar Mascotas")
        print("2. Mostrar Mascota")
        print("3. Agregar Mascota")
        print("4. Modificar Mascota")
        print("5. Eliminar Mascota")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Listar Mascotas
            self.listar_mascota()
        elif opcion == "2":  # Mostrar Mascota
            self.__mascota_controlador.mostrar()
        elif opcion == "3":  # Agregar Mascota
            self.__mascota_controlador.agregar()
        elif opcion == "4":  # Modificar Mascota
            self.__mascota_controlador.modificar()
        elif opcion == "5":  # Eliminar Mascota
            self.__mascota_controlador.eliminar()
        else:
            print("Opción inválida. Intente de nuevo.")

    def mostrar_mensaje(self, mensaje):
        # Mostrar un mensaje
        print(mensaje)

    def mostrar_lista_mascota(self, mascotas):
        # Mostrar la lista de mascotas
        self.limpiar_consola()
        for mascota in mascotas:
            print(f"{mascota.id}. {mascota.nombre}")

    def mostrar_mascota(self, mascota):
        # Mostrar los detalles de una mascota
        self.limpiar_consola()
        print("ID:", mascota.id)
        print("Nombre:", mascota.nombre)
        print("Especie:", mascota.especie)
        print("Raza:", mascota.raza)
        print("Color:", mascota.color)
        print("Peso:", mascota.peso)

    def obtener_datos_mascota(self):
        # Obtener los datos de una nueva mascota
        self.limpiar_consola()
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        color = input("Color: ")
        peso = float(input("Peso: "))
        return [id, nombre, especie, raza, color, peso]

    def obtener_datos_mascota_modificar(self):
        # Obtener los datos actualizados de una mascota
        self.limpiar_consola()
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        color = input("Color: ")
        peso = float(input("Peso: "))
        return [nombre, especie, raza, color, peso]

    def obtener_id(self):
        # Obtener el ID de una mascota
        self.limpiar_consola()
        return int(input("Ingrese el ID de la mascota: "))

    def listar_mascota(self):
        # Listar todas las mascotas
        mascotas = self.__mascota_modelo.listar()
        self.mostrar_lista_mascota(mascotas)
        self.mostrar_menu()

    def limpiar_consola(self):
        # Limpiar la consola según el sistema operativo
        if os.name == 'posix':  # Linux/Unix/MacOS
            _ = os.system('clear')
        elif os.name == 'nt':  # Windows
            _ = os.system('cls')
