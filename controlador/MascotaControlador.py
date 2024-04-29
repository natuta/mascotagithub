from modelo.MascotaModelo import MascotaModelo

class MascotaControlador:
    def __init__(self, mascota_vista):
        self.mascota_modelo = MascotaModelo()
        self.mascota_vista = mascota_vista

    def listar(self):
        mascotas = self.mascota_modelo.listar()
        if mascotas is not None:  # Verifica si la lista de mascotas no es None
            return mascotas
        else:
            return []  # Devuelve una lista vacía si la lista de mascotas es None


    

    def listar(self):
        mascotas = self.mascota_modelo.listar()
        if mascotas is not None:  # Verifica si la lista de mascotas no es None
            return mascotas
        else:
            return []  # Devuelve una lista vacía si la lista de mascotas es None



    def mostrar(self, id):
        mascota = self.mascota_modelo.buscar(id)
        if mascota is not None:
            self.mascota_vista.mostrar_mascota(mascota)

    def agregar(self, nombre, especie, raza, color, peso, persona):
    # Obtener el próximo ID disponible
        proximo_id = self.mascota_modelo.obtener_proximo_id()
        self.mascota_modelo.guardar(proximo_id, nombre, especie, raza, color, peso, persona)
        self.mascota_vista.mostrar_mensaje("La información se guardó correctamente.")
        self.mascota_vista.limpiar_formulario()
        self.listar()  # Después de agregar, volvemos a listar las mascotas actualizadas


    def modificar(self, id):
        datos_mascota = self.mascota_vista.obtener_datos_mascota_modificar()
        if datos_mascota is not None:  # Verificar si se obtuvieron los datos correctamente
            self.mascota_modelo.modificar(id, *datos_mascota)  # Pasar todos los datos obtenidos
            self.mascota_vista.mostrar_mensaje("La información se modificó correctamente.")
            self.listar()  # Después de modificar, volvemos a listar las mascotas actualizadas


    def eliminar(self, id):
        self.mascota_modelo.eliminar(id)
        self.mascota_vista.mostrar_mensaje("Se eliminó correctamente.")
        mascotas = self.listar()  # Obtener la lista actualizada de mascotas
        self.mascota_vista.mostrar_lista_mascotas(mascotas)  # Pasar la lista actualizada a la vista





