#from tkinter import *
import customtkinter as ctk
import os
import time

class main():
    def __init__(self,master):
        self.ledsBotton=[0]
        self.ledsOn=['#64B5F6']
        self.ledsOff=['#0A2463']

        self.canvas = ctk.CTkCanvas(master,width=1100,height=650,highlightthickness=0,relief='ridge',background="#1C1B1F")
        self.canvas.place(x=0,y=0)
        
          #Velocidad
        self.canvas.create_rectangle(350, 50, 750, 450, fill='red')
          #Direccion
        self.canvas.create_rectangle(350, 500, 750, 630, fill='blue')
          #Luces Frentes (led0)
        #self.canvas.create_rectangle(25, 50, 275, 150, fill='yellow')
        self.ledsFront = ctk.CTkButton(self.canvas, text="Leds Frente (off)",width=250,height=100,fg_color='#0A2463', hover_color='#467eac', command=self.ledsS(0))
        self.ledsFront.place(x=25,y=50)
          #Luces de freno
        #self.canvas.create_rectangle(25, 175, 275, 275, fill='red')
        self.ledsRear = ctk.CTkButton(self.canvas, text="Leds Traseras",width=250,height=100,fg_color='red')
        self.ledsRear.place(x=25,y=175)
          #Direccional derecha
        self.canvas.create_rectangle(25, 300, 150, 400, fill='orange')
          #Direccional izquierda
        self.canvas.create_rectangle(150, 300, 275, 400, fill='orange')
          #%Bateria
        self.canvas.create_rectangle(150, 425, 275, 625, fill='green')
          #%Luz
        self.canvas.create_rectangle(25, 425, 150, 625, fill='green')
          #Circulo
        self.label_Nom = ctk.CTkLabel(self.canvas, text="Por favor dijite su nombre: ", font= ("Cascadia Code",10),fg_color="red")
        self.label_Nom.place(x=30, y=70)
          #Reccorido infinito
          #ZIGZIG
          #Especial

    def ledsS(self,num):
        if self.ledsBotton[num]==0:
            print('hola')
            self.label_Nom.configure(text="new text")
            #self.ledsFront['fg_color']=self.ledsOn[0]
        #else:
            #self.ledsFront['text']="Leds Frente (off)"
            #self.ledsFront['fg_color']=self.ledsOff[0]
#Hola

Window=ctk.CTk()
ventana_principal=main(Window)
Window.title("Ezquisoneta")
Window.minsize(1100,650)
Window.mainloop()
