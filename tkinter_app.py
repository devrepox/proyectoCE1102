#from tkinter import *
import customtkinter as ctk
import os
import time

class main():
    def __init__(self,master):
        self.canvas = ctk.CTkCanvas(master,width=1100,height=650,highlightthickness=0,relief='ridge',background="#1C1B1F")
        self.canvas.place(x=0,y=0)
        
          #Velocidad
        self.canvas.create_rectangle(350, 50, 750, 450, fill='red')
          #Direccion
        self.canvas.create_rectangle(350, 500, 750, 630, fill='blue')
          #Luces Frentes
        self.canvas.create_rectangle(25, 50, 275, 150, fill='yellow')
          #Luces de freno
        self.canvas.create_rectangle(25, 175, 275, 275, fill='red')
          #Direccional derecha
        self.canvas.create_rectangle(25, 300, 150, 400, fill='orange')
          #Direccional izquierda
        self.canvas.create_rectangle(150, 300, 275, 400, fill='orange')
          #%Bateria
        self.canvas.create_rectangle(150, 425, 275, 625, fill='green')
          #%Luz
        self.canvas.create_rectangle(25, 425, 150, 625, fill='green')
          #Circulo
          #Reccorido infinito
          #ZIGZIG
          #Especial

#Hola

Window=ctk.CTk()
ventana_principal=main(Window)
Window.title("Ezquisoneta")
Window.minsize(1100,650)
Window.mainloop()
