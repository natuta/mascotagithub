import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controlador.MascotaControlador import MascotaControlador

from modelo.MascotaModelo import MascotaModelo

class MascotaVista:
    def __init__(self):
        self._mascota_controlador= MascotaControlador(self)
        self._mascota_modelo=MascotaModelo()
        self.root = tk.Tk()
        self.root.title("CRUD Mascota")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Gestión de Mascotas")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_nombre = tk.Label(self.frame, text="Nombre:", justify="left")
        self.label_nombre.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self.frame, width=50)
        self.entry_nombre.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        self.label_especie = tk.Label(self.frame, text="Especie:", justify="left")
        self.label_especie.grid(row=2, column=0, padx=5, pady=5)
        self.entry_especie = tk.Entry(self.frame, width=50)
        self.entry_especie.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

        self.label_raza = tk.Label(self.frame, text="Raza:", justify="left")
        self.label_raza.grid(row=3, column=0, padx=5, pady=5)
        self.entry_raza = tk.Entry(self.frame, width=50)
        self.entry_raza.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

        self.label_color = tk.Label(self.frame, text="Color:", justify="left")
        self.label_color.grid(row=4, column=0, padx=5, pady=5)
        self.entry_color = tk.Entry(self.frame, width=50)
        self.entry_color.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        self.label_peso = tk.Label(self.frame, text="Peso:", justify="left")
        self.label_peso.grid(row=5, column=0, padx=5, pady=5)
        self.entry_peso = tk.Entry(self.frame, width=50)
        self.entry_peso.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
        
        self.label_persona = tk.Label(self.frame, text="Carné de la Persona:", justify="left")
        self.label_persona.grid(row=6, column=0, padx=5, pady=5)
        self.entry_persona = tk.Entry(self.frame, width=50)
        self.entry_persona.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

        self.btn_listar = tk.Button(self.frame, text="Listar Mascotas", command=self.listar_mascotas)
        self.btn_listar.grid(row=7, column=0, padx=5, pady=5)
        self.btn_agregar = tk.Button(self.frame, text="Agregar Mascota", command=self.agregar_mascota)
        self.btn_agregar.grid(row=7, column=1, padx=5, pady=5)
        self.btn_modificar = tk.Button(self.frame, text="Modificar Mascota", command=self.modificar_mascota)
        self.btn_modificar.grid(row=7, column=2, padx=5, pady=5)
        self.btn_eliminar = tk.Button(self.frame, text="Eliminar Mascota", command=self.eliminar_mascota)
        self.btn_eliminar.grid(row=7, column=3, padx=5, pady=5)

        self.treeview = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Especie"),
                                     show="headings")
        self.treeview.grid(row=8, column=0, columnspan=4)

        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Especie", text="Especie")
        self.treeview.bind("<ButtonRelease-1>", self.mostrar_mascota_seleccionada)

        
        self.root.mainloop()

    def listar_mascotas(self):
         for row in self.treeview.get_children():
            self.treeview.delete(row)
            mascotas = self.mascota_controlador.listar()
            for mascota in mascotas:
                self.treeview.insert("", "end", values=(mascota.id, mascota.nombre, mascota.especie))
       
      

    def mostrar_lista_mascotas(self, mascotas):
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for mascota in mascotas:
            self.treeview.insert("", "end", values=(mascota.id, mascota.nombre, mascota.especie))

    def mostrar_mascota(self, mascota):
        self.limpiar_formulario()
        self.entry_nombre.insert(tk.END, mascota.nombre)
        self.entry_especie.insert(tk.END, mascota.especie)
        self.entry_raza.insert(tk.END, mascota.raza)
        self.entry_color.insert(tk.END, mascota.color)
        self.entry_peso.insert(tk.END, mascota.peso)
        self.entry_persona.insert(tk.END, mascota.persona)

    def obtener_datos_mascota(self):
        nombre = self.entry_nombre.get()
        especie = self.entry_especie.get()
        raza = self.entry_raza.get()
        color = self.entry_color.get()
        peso = float(self.entry_peso.get())
        persona = int(self.entry_persona.get())
        return [nombre, especie, raza, color, peso, persona]


    def obtener_datos_mascota_modificar(self):
        nombre = self.entry_nombre.get()
        especie = self.entry_especie.get()
        raza = self.entry_raza.get()
        color = self.entry_color.get()
        peso = float(self.entry_peso.get())
        persona = int(self.entry_persona.get())
        return [nombre, especie, raza, color, peso, persona]

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Éxito", mensaje)

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_especie.delete(0, tk.END)
        self.entry_raza.delete(0, tk.END)
        self.entry_color.delete(0, tk.END)
        self.entry_peso.delete(0, tk.END)
        self.entry_persona.delete(0, tk.END)

    def mostrar_mascota_seleccionada(self, event):
        item = self.treeview.selection()
        if item:
           item = item[0]
           id = self.treeview.item(item, "values")[0]
           mascota = self.mascota_controlador.mostrar(id)
        if mascota:
            self.mostrar_mascota(mascota)

    def agregar_mascota(self):
        datos_mascota = self.obtener_datos_mascota()
        self._mascota_controlador.agregar(*datos_mascota)
        self.listar_mascotas()  # Después de agregar, volvemos a listar las mascotas actualizadas


    def modificar_mascota(self):
        item = self.treeview.selection()
        if item:
            item = item[0]
            id = self.treeview.item(item, "values")[0]
            datos_mascota = self.obtener_datos_mascota_modificar()
            self.mascota_controlador.modificar(id, *datos_mascota)
            self.listar_mascota()  # Después de modificar, volvemos a listar las mascotas actualizadas

    def eliminar_mascota(self):
        item = self.treeview.selection()
        if item:
            item = item[0]
            id = self.treeview.item(item, "values")[0]
            self.mascota_controlador.eliminar(id)
            self.listar_mascota()  # Después de eliminar, volvemos a listar las mascotas actualizadas
