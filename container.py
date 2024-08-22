from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1000, height=500)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

#interfaz grafica del proyecto.#
    #interfaz grafica del proyecto.#
    def widgets(self):

        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)
        
        # Botón ventas
        btnventas = Button(frame1, bg="#f4b400", fg="white", text="Ir a ventas", font=("Arial", 14), command=self.ventas)
        btnventas.place(x=50, y=30, width=240, height=60)

        # Botón inventario
        btninventario = Button(frame1, bg="#c62e26", fg="white", text="Ir a Inventario", font=("Arial", 14), command=self.inventario)
        btninventario.place(x=50, y=130, width=240, height=60)

        # Logo y parámetros
        self.logo_image = Image.open("imagenes/marca-de-comidas.jpg.webp")
        self.logo_image = self.logo_image.resize((300, 300))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=464, y=30)

        # Label de copyright
        copyright_label = tk.Label(frame1, text="Creado 2024 CajaRegistradora - Jonathan Curiñan. Todos los derechos reservados", font=("Arial", 10), bg="gray", fg="white")

        # Coloca el mensaje de copyright en la parte inferior y centrado
        copyright_label.place(x=50, y=350, width=700, height=30)
