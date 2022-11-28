from cProfile import label
from cgitb import text
import tkinter as tk
from random import shuffle

from pygame import font
#haznelerden true olanda kurşun var
gun =[False,True,False,False,False,False]

#Ana pencere görüntüsü
root=tk.Tk()
root.title("Rus Ruletine Hoşgeldin Babuş")
root.geometry("500x400")
p1=tk.PhotoImage(file='tabanca.png')
root.iconphoto(False,p1)

#yazımızın değişkeni ve yazımızın yerleştirilmesi

label=tk.Label(root,text="Ateş Et!!!",font=("Arial",20),pady=20)
label.pack()

#Hazneleri random karıştırma
def ates_haznesi():
    shuffle(gun)
    button1.config(state="normal")
    button2.config(state="normal")
    label.config(text="Ateş Et!!!")
#Ates etme fonksiyonu
def ates():
    if gun[0]:
        label.config(text="Öldün ")
        button1.config(state="disabled")
        button2.config(state="disabled")
    else:
        label.config(text="Pacayı Yırttın ")
        button2.config(state="disabled")
#karıstıma buttonu
button1=tk.Button(root,text="Karıştır",command=ates_haznesi,font=("Arial",20))
button1.pack()

#Ateş etme buttonu
button2=tk.Button(root,text="Ateş Et",command=ates,font=("Arial",20))
button2.pack()

# pencereyi göstermekomutu
root.mainloop()