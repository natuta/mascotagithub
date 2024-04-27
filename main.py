from vista.MascotaVistaTkinter import MascotaVista
from controlador.MascotaControlador import MascotaControlador

if __name__ == "__main__":
    vista = MascotaVista()  
    controlador = MascotaControlador(vista)  # Pasar la instancia de MascotaVista al crear MascotaControlador
