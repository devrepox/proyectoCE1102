#from tkinter import *
import time
from tkinter import messagebox
from customtkinter import *
from threading import Thread 
from PIL import Image

from WiFiClient import NodeMCU

class main():
    def __init__(self,master):
        #Motor
        self.motor=0

        #Atributos referentes a los botones (colores, iconos y estados)
        self.ledsBotton=[0,0,0,0]
        self.ledsHover=['#056EC3','#D20f00','#565351']
        self.ledsOff=['#030e27','#7b0700','#292726']
        self.ledsOn=['#056EC3','#E21404','#34312F']
        
        #Variables con los iconos
        self.ledsIco=[CTkImage(Image.open("assets/ledOff.png"),size=(64,64)),CTkImage(Image.open("assets/ledonFront.png"),size=(64,64)),CTkImage(Image.open("assets/ledOnBack.png"),size=(64,64))]
        self.dirIco=[CTkImage(Image.open("assets/LedDerOff.png"),size=(64,64)),CTkImage(Image.open("assets/LedDerOn.png"),size=(64,64)),CTkImage(Image.open("assets/LedIzqOff.png"),size=(64,64)),CTkImage(Image.open("assets/LedIzqOn.png"),size=(64,64))]
        self.letraA=CTkImage(Image.open("assets/a.png"),size=(64,64))
        self.letraN=CTkImage(Image.open("assets/n.png"),size=(64,64))
        self.letraR=CTkImage(Image.open("assets/r.png"),size=(64,64))
        self.flechaIzq=CTkImage(Image.open("assets/dirIzq.png"),size=(64,64))
        self.flechaDer=CTkImage(Image.open("assets/dirDer.png"),size=(64,64))
        self.volanteIco=CTkImage(Image.open("assets/volante.png"),size=(64,64))
        self.batIcon=CTkImage(Image.open("assets/bateria.png"),size=(48,48))
        self.ResIcon=CTkImage(Image.open("assets/resistor.png"),size=(48,48))
        #Crear el canvas
        self.canvas = CTkCanvas(master,width=1100,height=650,highlightthickness=0,relief='ridge',background="#1C1B1F")
        self.canvas.place(x=0,y=0)
     
        #Cuadro de lectura del log
        self.logSpace= CTkLabel(self.canvas, text="Log", fg_color="black", height=100, width=250)
        self.logSpace.place(x=800,y=50)

        #Cuadros de marchas con valores (0,50,100,150,200,250)
        self.Marcha0 = CTkButton(self.canvas, text="0",text_color="#312F2F",command=lambda:self.setMarcha(0),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha0.place(x=375,y=60)
        self.Marcha1 = CTkButton(self.canvas, text="50",text_color="#312F2F",command=lambda:self.setMarcha(50),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha1.place(x=375,y=120)
        self.Marcha2 = CTkButton(self.canvas, text="100",text_color="#312F2F",command=lambda:self.setMarcha(100),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha2.place(x=375,y=180)
        self.Marcha3 = CTkButton(self.canvas, text="150",text_color="#312F2F",command=lambda:self.setMarcha(150),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha3.place(x=375,y=240)
        self.Marcha4 = CTkButton(self.canvas, text="200",text_color="#312F2F",command=lambda:self.setMarcha(200),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha4.place(x=375,y=300)
        self.Marcha5 = CTkButton(self.canvas, text="250",text_color="#312F2F",command=lambda:self.setMarcha(250),width=50,height=50,fg_color="#EFF2F1", hover=FALSE,compound=RIGHT)
        self.Marcha5.place(x=375,y=360)
        #Cuadro de marcha seleccionada que cambia de acuerdo a la selección
        self.MarchaSelect = CTkButton(self.canvas, text="0",text_color="#DCEDFF",font=('CTkDefaultFont',24),width=50,height=50,fg_color="#426A5A", hover=FALSE,compound=RIGHT)
        self.MarchaSelect.place(x=375,y=430)

        #Cuadros con las velocidades (adelante, atrás, neutro)
        self.AdelanteB = CTkButton(self.canvas, text="Adelante",command=lambda:self.setDirection("Adelante",1),width=250,height=110,fg_color=self.ledsOff[2], hover=FALSE,compound=TOP,image=self.letraA)
        self.AdelanteB.place(x=450,y=60)
        self.StopB = CTkButton(self.canvas, text="Neutro",command=lambda:self.setDirection("Neutro",0),width=250,height=110,fg_color=self.ledsOff[2], hover=FALSE,compound=TOP, image=self.letraN)
        self.StopB.place(x=450,y=180)
        self.AtrasB = CTkButton(self.canvas, text="Reversa",command=lambda:self.setDirection("Reversa",-1),width=250,height=110,fg_color=self.ledsOff[2], hover=FALSE,compound=TOP, image=self.letraR)
        self.AtrasB.place(x=450,y=300)
        #Direccion seleccionada de acuerdo a los botones anteriores
        self.SelectDir = CTkButton(self.canvas, text="Neutro",text_color="#DCEDFF",font=('CTkDefaultFont',24),width=250,height=50,fg_color="#9B1D20", hover=FALSE,compound=RIGHT)
        self.SelectDir.place(x=450,y=430)

        #Botones de direccion Direccion(iz1[-1],centro[0],der[1])
        self.RuedaIzq = CTkButton(self.canvas, text="",command=lambda:self.doblar(-1),width=130,height=130,fg_color=self.ledsOff[2], hover=FALSE,compound=RIGHT,image=self.flechaIzq)
        self.RuedaIzq.place(x=350,y=500)
        self.RuedaCent = CTkButton(self.canvas, text="",command=lambda:self.doblar(0),width=130,height=130,fg_color=self.ledsOff[2], hover=FALSE,compound=RIGHT,image=self.volanteIco)
        self.RuedaCent.place(x=485,y=500)
        self.RuedaDer = CTkButton(self.canvas, text="",command=lambda:self.doblar(1),width=130,height=130,fg_color=self.ledsOff[2], hover=FALSE,compound=RIGHT,image=self.flechaDer)
        self.RuedaDer.place(x=620,y=500)
        
        #Luces Frentes (led0, pines: 5,6)
        self.ledsOffIco=CTkImage(Image.open("assets/ledOff.png"),size=(64,64))
        self.ledsFront = CTkButton(self.canvas, text="Leds Frente",command=lambda:[self.ledSF()],width=250,height=100,fg_color=self.ledsOff[0], hover=FALSE, image=self.ledsOffIco, compound=RIGHT)
        self.ledsFront.place(x=25,y=50)
          
        #Luces de freno (led1, pines:1,2)
        self.ledsRear = CTkButton(self.canvas, text="Leds Trasero",command=self.ledSB,width=250,height=100,fg_color=self.ledsOff[1], hover=FALSE,image=self.ledsOffIco, compound=RIGHT)
        self.ledsRear.place(x=25,y=175)
          
        #Direccional Izq(pin:3)
        self.ledsDI = CTkButton(self.canvas,text="",command=self.ledSDI,width=125,height=75,fg_color=self.ledsOff[2],hover=FALSE,image=self.dirIco[2])
        self.ledsDI.place(x=25,y=300)
          
        #Direccional Der(pin:?)
        self.ledsDD = CTkButton(self.canvas,text="",command=self.ledSDD,width=125,height=75,fg_color=self.ledsOff[2],hover=FALSE,image=self.dirIco[0])
        self.ledsDD.place(x=150,y=300)

        #CONTROL MAESTRO LUCES
        self.ledsALLON = CTkButton(self.canvas,text="",width=125,height=75,fg_color=self.ledsOff[2],hover=FALSE,image=self.ledsIco[1],command=lambda:send("ledson;"))
        self.ledsALLON.place(x=25,y=400)
        self.ledsALLOFF = CTkButton(self.canvas,text="",width=125,height=75,fg_color=self.ledsOff[2],hover=FALSE,image=self.ledsIco[0],command=lambda:send("ledsoff;"))
        self.ledsALLOFF.place(x=150,y=400)

        #%Bateria
        self.WidgetBatery = CTkButton(self.canvas, text="Bateria",command=self.indicadorSB,width=125,height=125,fg_color=self.ledsOff[2], hover=FALSE, image=self.batIcon,compound=TOP)
        self.WidgetBatery.place(x=150,y=500)
        #%Luz
        self.WidgetFotoResistencia = CTkButton(self.canvas, text="Ind Luz",command=self.indicadorSL,width=125,height=125,fg_color=self.ledsOff[2], hover=FALSE, image=self.ResIcon,compound=TOP)
        self.WidgetFotoResistencia.place(x=25,y=500)
          
          #Circulo
          #Reccorido infinito
          #ZIGZIG
          #Especial
    
    #Funciones de los botones
    def ledSF(self):
        if self.ledsBotton[0]==0:
            self.ledsBotton[0]=1
            self.ledsFront.configure(fg_color=self.ledsOn[0])
            self.ledsFront.configure(image=self.ledsIco[1])
            send("lf:1;")
        else:
            self.ledsBotton[0]=0
            self.ledsFront.configure(fg_color=self.ledsOff[0])
            self.ledsFront.configure(image=self.ledsIco[0])
            send("lf:0;")
    def ledSB(self):
        if self.ledsBotton[1]==0:
            self.ledsBotton[1]=1

            self.ledsRear.configure(fg_color=self.ledsOn[1])
            self.ledsRear.configure(image=self.ledsIco[2])
            send("lb:1;")

        else:
            self.ledsBotton[1]=0
            self.ledsRear.configure(fg_color=self.ledsOff[1])
            self.ledsRear.configure(image=self.ledsIco[0])
            send("lb:0;")
    def ledSDI(self):
        if self.ledsBotton[2]==0:
            self.ledsBotton[2]=1
            self.ledsDI.configure(fg_color=self.ledsOn[2])
            self.ledsDI.configure(image=self.dirIco[3])
            send("ll:1;")
        else:
            self.ledsBotton[2]=0
            self.ledsDI.configure(fg_color=self.ledsOff[2])
            self.ledsDI.configure(image=self.dirIco[2])
            send("ll:0;")
    def ledSDD(self):
        if self.ledsBotton[3]==0:
            self.ledsBotton[3]=1
            self.ledsDD.configure(fg_color=self.ledsOn[2])
            self.ledsDD.configure(image=self.dirIco[1])
            send("lr:1;")
        else:
            self.ledsBotton[3]=0
            self.ledsDD.configure(fg_color=self.ledsOff[2])
            self.ledsDD.configure(image=self.dirIco[0])
            send("lr:10;")
    def indicadorSB(self):
        pass
    def indicadorSL(self):
        print("indicador luz")
    def setMarcha(self,v):
        self.MarchaSelect.configure(text=str(v))
        self.pwmv=v*self.motor
        print(str(self.pwmv))
        send("pwm:"+str(self.pwmv)+";")
    def setDirection(self,d,v):
        self.SelectDir.configure(text=str(d))
        self.motor=v
        
    def doblar(self,v):
        send("dir:"+str(v)+";")
    def updateLog(self,msg):
        self.logSpace.configure(text=str(msg))
        
        

#           _____________________________________
#__________/Creando el cliente para NodeMCU
myCar = NodeMCU()
myCar.start()


def get_log():
    """
    Hilo que actualiza los Text cada vez que se agrega un nuevo mensaje al log de myCar
    """
    indice = 0
    # Variable del carro que mantiene el hilo de escribir.
    while(myCar.loop):
        while(indice < len(myCar.log)):
            mnsSend = "[{0}] cmd: {1}\n".format(indice,myCar.log[indice][0])
            #SentCarScrolledTxt.insert(END,mnsSend)
            #SentCarScrolledTxt.see("end")

            mnsRecv = "[{0}] result: {1}\n".format(indice,myCar.log[indice][1])
            ventana_principal.updateLog(mnsRecv)
            #RevCarScrolledTxt.insert(END, mnsRecv)
            #RevCarScrolledTxt.see('end')

            indice+=1
        time.sleep(0.200)
    
p = Thread(target=get_log)
p.start()
           
def send (event):
    """
    Ejemplo como enviar un mensaje sencillo sin importar la respuesta
    """
    mns = str(event)
    if(len(mns)>0 and mns[-1] == ";"):
        myCar.send(mns)
    else:
        messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')") 

Window=CTk()
ventana_principal=main(Window)
Window.title("Ezquisoneta")
Window.minsize(1100,650)
Window.bind('<Return>', send) #Vinculando tecla Enter a la función send
Window.mainloop()
