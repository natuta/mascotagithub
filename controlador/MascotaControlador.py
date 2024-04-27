from modelo.MascotaModelo import MascotaModelo

class MascotaControlador:

    def __init__(self, mascota_vista):
        self.mascota_modelo = MascotaModelo()
        self.mascota_vista = mascota_vista

    def listar(self):
        mascotas = self.mascota_modelo.listar()
        self.mascota_vista.mostrar_lista_mascota(mascotas)

    def mostrar(self, id):
        mascota = self.mascota_modelo.buscar(id)
        if mascota is not None:
            self.mascota_vista.mostrar_mascota(mascota)

    def agregar(self, nombre, especie, raza, color, peso, persona):
        self.mascota_modelo.guardar(nombre, especie, raza, color, peso, persona)
    # Resto del código...
        self.mascota_vista.mostrar_mensaje("La información se guardó correctamente.")
        self.mascota_vista.limpiar_formulario()
        self.listar()  # Después de agregar, volvemos a listar las mascotas actualizadas


    def modificar(self, id):
        mascota = self.mascota_vista.obtener_datos_mascota_modificar()
        self.mascota_modelo.modificar(mascota[0], mascota[1], mascota[2], mascota[3])
        self.mascota_vista.mostrar_mensaje("La información se modificó correctamente.")
        self.mascota_vista.mostrar_lista_mascota()

    def eliminar(self, id):
        self.mascota_modelo.eliminar(id)
        self.mascota_vista.mostrar_mensaje("Se eliminó correctamente.")
        self.mascota_vista.mostrar_lista_mascota()
        self.mascota_vista.limpiar_formulario()