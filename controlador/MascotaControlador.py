from modelo.MascotaModelo import MascotaModelo

class MascotaControlador:

    def __init__(self, mascota_vista):
        self.mascota_modelo = MascotaModelo()
        self.mascota_vista = mascota_vista

    def listar(self):
        # Listar todas las mascotas
        mascotas = self.mascota_modelo.listar()
        self.mascota_vista.mostrar_lista_mascota(mascotas)
        self.mascota_vista.mostrar_menu()

    def mostrar(self):
        # Mostrar los detalles de una mascota
        id = self.mascota_vista.obtener_id()
        mascota = self.mascota_modelo.buscar(id)
        if mascota is not None:
            self.mascota_vista.mostrar_mascota(mascota)
        self.mascota_vista.mostrar_menu()

    def agregar(self):
        # Agregar una nueva mascota
        datos_mascota = self.mascota_vista.obtener_datos_mascota()
        self.mascota_modelo.guardar(*datos_mascota)
        self.mascota_vista.mostrar_mensaje("La mascota se agregó correctamente.")
        self.mascota_vista.mostrar_menu()

    def modificar(self):
        # Modificar los detalles de una mascota existente
        id = self.mascota_vista.obtener_id()
        datos_mascota = self.mascota_vista.obtener_datos_mascota_modificar()
        self.mascota_modelo.modificar(id, *datos_mascota)
        self.mascota_vista.mostrar_mensaje("La información de la mascota se modificó correctamente.")
        self.mascota_vista.mostrar_menu()

    def eliminar(self):
        # Eliminar una mascota
        id = self.mascota_vista.obtener_id()
        self.mascota_modelo.eliminar(id)
        self.mascota_vista.mostrar_mensaje("La mascota se eliminó correctamente.")
        self.mascota_vista.mostrar_menu()
