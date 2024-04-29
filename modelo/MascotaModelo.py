import os
import csv

class Mascota:
    def __init__(self, id, nombre, especie, raza, color, peso, persona):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.color = color
        self.peso = peso
        self.persona = persona

class MascotaModelo:
    def __init__(self):
        self.__archivo = "mascotas.csv"
        self.__lista = []
        self.__cargar_lista()

    def __guardar_lista(self):
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for mascota in self.__lista:
                writer.writerow([mascota.id, mascota.nombre, mascota.especie, mascota.raza, mascota.color, mascota.peso, mascota.persona])

    def __cargar_lista(self):
        try:
            self.__lista = []
            with open(self.__archivo, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row and row[0].strip().isdigit():
                        if len(row) == 7:
                            id, nombre, especie, raza, color, peso, persona = row
                            mascota = Mascota(int(id), nombre, especie, raza, color, float(peso), int(persona))
                            self.__lista.append(mascota)
                        else:
                            print(f"Advertencia: La línea '{row}' no contiene todos los atributos de la mascota.")
        except FileNotFoundError:
            self.__lista = []

    

    def listar(self):
        self.__cargar_lista()  # Llama a __cargar_lista() para cargar la lista de mascotas
        return self.__lista


    def buscar(self, id):
        self.__cargar_lista()
        for mascota in self.__lista:
            if mascota.id == id:
                return mascota
        return None

    def guardar(self, id, nombre, especie, raza, color, peso, persona):
        mascota = Mascota(id, nombre, especie, raza, color, peso, persona)
        self.__lista.append(mascota)
        self.__guardar_lista()

    def obtener_proximo_id(self):
        self.__cargar_lista()
        if self.__lista:
            ultimo_id = max(mascota.id for mascota in self.__lista)
            return ultimo_id + 1
        else:
            return 1


    def modificar(self, id, nombre, especie, raza, color, peso, persona):
        for mascota in self.__lista:
            if mascota.id == id:
                mascota.nombre = nombre
                mascota.especie = especie
                mascota.raza = raza
                mascota.color = color
                mascota.peso = peso
                mascota.persona = persona
                self.__guardar_lista()
                return


    def eliminar(self, id):
        for mascota in self.__lista:
            if mascota.id == id:
                self.__lista.remove(mascota)
                self.__guardar_lista()
                return


