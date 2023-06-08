from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter as ctk

class Main():
    def __init__(self,master):
        self.ledsBotton=[0]
        self.ledsOn=['#64B5F6']
        self.ledsOff=['#0A2463']

        self.canvas=CTkCanvas(master,width=750,height=500,highlightthickness=0,relief='ridge')
        self.canvas.place(x=0,y=0)

        self.button=CTkButton(self.canvas,text="Hola",command=self.button_function,width=100,height=80)
        self.button.place(x=750/2,y=500/2)

        self.ledsFront = CTkButton(self.canvas, text="Leds Frente (off)",command=self.ledSF,width=250,height=100,fg_color='#0A2463', hover_color='#467eac')
        self.ledsFront.place(x=25,y=50)
    
    def button_function(self):
        print("Hola")
        self.button.configure(text="Adios")
    
    def ledSF(self):
        if self.ledsBotton[0]==0:
            self.ledsBotton[0]=1
            print("Prende")
            self.ledsFront.configure(text="Leds Frente (on)")
            self.ledsFront.configure(fg_color=self.ledsOn[0])
        else:
            self.ledsBotton[0]=0
            print("Apaga")
            self.ledsFront.configure(text="Leds Frente (off)")
            self.ledsFront.configure(fg_color=self.ledsOff[0])

window=CTk()
pantallaprincipal=Main(window)
window.title("Taller_Tkinter")
window.minsize(750,500)
window.resizable(False,False)
window.mainloop()
