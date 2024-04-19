import os
import csv

class Mascota:
    def __init__(self, id, nombre, especie, raza, color, peso):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.color = color
        self.peso = peso

class MascotaModelo:
    def __init__(self):
        # Definición del archivo CSV donde se almacenarán los datos
        self.__archivo = "mascotas.csv"
        # Lista para almacenar las mascotas
        self.__lista = []
        # Cargar la lista de mascotas desde el archivo al inicializar
        self.__cargar_lista()

    def __guardar_lista(self):
        # Guardar la lista de mascotas en el archivo CSV
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for mascota in self.__lista:
                writer.writerow([mascota.id, mascota.nombre, mascota.especie, mascota.raza, mascota.color, mascota.peso])

    def __cargar_lista(self):
        try:
            self.__lista = []
            with open(self.__archivo, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    # Verificar si la línea comienza con un número
                    if row and row[0].strip().isdigit():
                        # Desempaquetar la fila si tiene datos de mascotas
                        if len(row) == 6:
                            id, nombre, especie, raza, color, peso = row
                            mascota = Mascota(int(id), nombre, especie, raza, color, float(peso))
                            self.__lista.append(mascota)
                        else:
                            print(f"Advertencia: La línea '{row}' no contiene todos los atributos de la mascota.")
        except FileNotFoundError:
            self.__lista = []




    def listar(self):
        # Devuelve la lista de todas las mascotas
        self.__cargar_lista()
        return self.__lista

    def buscar(self, id):
        # Busca una mascota por su ID y la devuelve, si no se encuentra, devuelve None
        self.__cargar_lista()
        for mascota in self.__lista:
            if int(mascota.id) == int(id):
                return mascota
        return None

    def guardar(self, id, nombre, especie, raza, color, peso):
        # Agrega una nueva mascota a la lista y guarda la lista actualizada
        mascota = Mascota(id, nombre, especie, raza, color, peso)
        self.__lista.append(mascota)
        self.__guardar_lista()

    def modificar(self, id, nombre, especie, raza, color, peso):
        # Modifica los detalles de una mascota existente y guarda la lista actualizada
        self.__cargar_lista()
        for mascota in self.__lista:
            if int(mascota.id) == int(id):
                mascota.nombre = nombre
                mascota.especie = especie
                mascota.raza = raza
                mascota.color = color
                mascota.peso = peso
                self.__guardar_lista()
                return

    def eliminar(self, id):
        # Elimina una mascota por su ID de la lista y guarda la lista actualizada
        self.__cargar_lista()
        for mascota in self.__lista:
            if int(mascota.id) == int(id):
                self.__lista.remove(mascota)
                self.__guardar_lista()
                self.__cargar_lista()
                return
