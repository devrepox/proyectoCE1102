#from tkinter import *
from customtkinter import *
import tkinter as tk
import os
import time

class main():
    print('Hola')
    def __init__(self,master):
        self.ledsBotton=[0,0,0,0]
        self.ledsOn=['#67a9dd','#FF3628','#565351']
        self.ledsOff=['#0A2463','#9F0B00','#292726']
        self.ledsHover=['#467eac','#C92A1F','#34312F']

        self.canvas = CTkCanvas(master,width=1100,height=650,highlightthickness=0,relief='ridge',background="#1C1B1F")
        self.canvas.place(x=0,y=0)
        
          #Velocidad
        self.canvas.create_rectangle(350, 50, 750, 450, fill='red')
          #Direccion
        self.canvas.create_rectangle(350, 500, 750, 630, fill='blue')
          #Luces Frentes (led0) (25, 50, 275, 150, fill='blue')
        self.ledsFront = CTkButton(self.canvas, text="Leds Frente (off)",command=self.ledSF,width=250,height=100,fg_color=self.ledsOff[0], hover_color=self.ledsHover[0])
        self.ledsFront.place(x=25,y=50)
          #Luces de freno (25, 175, 275, 275, fill='red')
        self.ledsRear = CTkButton(self.canvas, text="Leds Trasero (off)",command=self.ledSB,width=250,height=100,fg_color=self.ledsOff[1], hover_color=self.ledsHover[1])
        self.ledsRear.place(x=25,y=175)
          #Direccional Izq
        #self.canvas.create_rectangle(25, 300, 150, 400, fill='orange')
        self.ledsDI = CTkButton(self.canvas, text="DirIzq",command=self.ledSDI,width=125,height=100,fg_color=self.ledsOff[2], hover_color=self.ledsHover[2])
        self.ledsDI.place(x=25,y=300)
          #Direccional Der
        #self.canvas.create_rectangle(150, 300, 275, 400, fill='orange')
        self.ledsDD = CTkButton(self.canvas, text="DirDer",command=self.ledSDD,width=125,height=100,fg_color=self.ledsOff[2], hover_color=self.ledsHover[2])
        self.ledsDD.place(x=150,y=300)
          #%Bateria
        self.canvas.create_rectangle(150, 425, 275, 625, fill='green')
          #%Luz
        self.canvas.create_rectangle(25, 425, 150, 625, fill='green')
          #Circulo
          #Reccorido infinito
          #ZIGZIG
          #Especial

    def ledSF(self):
        if self.ledsBotton[0]==0:
            self.ledsBotton[0]=1
            self.ledsFront.configure(text="Leds Frente (on)")
            self.ledsFront.configure(fg_color=self.ledsOn[0])
        else:
            self.ledsBotton[0]=0
            self.ledsFront.configure(text="Leds Frente (off)")
            self.ledsFront.configure(fg_color=self.ledsOff[0])
    def ledSB(self):
        if self.ledsBotton[1]==0:
            self.ledsBotton[1]=1
            self.ledsRear.configure(text="Leds Trasero (on)")
            self.ledsRear.configure(fg_color=self.ledsOn[1])
        else:
            self.ledsBotton[1]=0
            self.ledsRear.configure(text="Leds Trasero (off)")
            self.ledsRear.configure(fg_color=self.ledsOff[1])
    def ledSDI(self):
        if self.ledsBotton[2]==0:
            self.ledsBotton[2]=1
            self.ledsDI.configure(fg_color=self.ledsOn[2])
        else:
            self.ledsBotton[2]=0
            self.ledsDI.configure(fg_color=self.ledsOff[2])
    def ledSDD(self):
        if self.ledsBotton[3]==0:
            self.ledsBotton[3]=1
            self.ledsDD.configure(fg_color=self.ledsOn[2])
        else:
            self.ledsBotton[3]=0
            self.ledsDD.configure(fg_color=self.ledsOff[2])


Window=CTk()
ventana_principal=main(Window)
Window.title("Ezquisoneta")
Window.minsize(1100,650)
Window.mainloop()
