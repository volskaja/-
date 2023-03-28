from msilib.schema import RadioButton
from tkinter import *
from math import *
from random import *
from tkinter import font 


def valik(): #можно поставить значение от которогог зависити функция
    num=var.get()
    if num == 1:
        raam1 = Tk()
        raam1.title("Tahvel")
        tahvel1 = Canvas(raam1, 
                width=250, 
                height=150, 
                background="white")
        tahvel1.create_rectangle(0,0, 250,150,fill="#4cacc2")
        tahvel1.create_rectangle(0,50, 250,150,fill="yellow")
        tahvel1.create_rectangle(0,100, 250,150,fill="#4cacc2")
        tahvel1.create_polygon(0,0, 110,75, 0,150, fill="black")
        tahvel1.grid()
        raam1.mainloop()
    elif num == 2:
        raam2 = Tk()
        raam2.title("Tahvel")
        tahvel2 = Canvas(raam2, 
                width=250, 
                height=150, 
                background="white")
        tahvel2.create_rectangle(0,0, 250,150,fill="blue")
        tahvel2.create_rectangle(0,50, 250,150,fill="black")
        tahvel2.create_rectangle(0,100, 250,150,fill="white")
        tahvel2.grid()
        raam2.mainloop()
    elif num == 3:
        raam3 = Tk()
        raam3.title("Tahvel")
        tahvel3 = Canvas(raam3, 
                width=250, 
                height=150, 
                background="white")
        tahvel3.create_rectangle(0,0, 250,150,fill="white")
        tahvel3.create_rectangle(0,73, 250,150,fill="red")
        tahvel3.grid()
        raam3.mainloop()
    elif num == 4:
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, 
                        width=600, 
                        height=600, 
                        background="white")
        x0=0
        y0=0
        x1=600
        y1=600
        a=300
        r=(a**2+a**2)**(1/2)
        p=(a-r)
        for i in range(12):
            x0+=p
            y0+=p
            x1-=p
            y1-=p
            tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue",fill="red")
            tahvel.create_oval(x0,y0,x1,y1,width=1,outline="blue",fill="yellow")
            p=r-a 
            r=r-p
            a=((r)*sqrt(2))/2
        tahvel.grid()
        raam.mainloop()
    elif num == 5:
        raam5 = Tk()
        raam5.title("Шахматная доска")
        tahvel5=Canvas(raam5, 
                       width=250, 
                       height=250, 
                       background="white")
        width=250
        height=250
        width1=int(width/8)
        height1=int(height/8)
        for row in range(8):
            for col in range(8):
                x1=col*width1
                y1=row*height1
                x2=x1+width1
                y2=y1+height1
                if (row+col) % 2 == 0:
                    tahvel5.create_rectangle(x1,y1,x2,y2,fill="white")
                else:
                    tahvel5.create_rectangle(x1,y1,x2,y2,fill="black")
        tahvel5.grid()
        raam5.mainloop()
    elif num == 6:
        colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "gray",
        "yellow",
        "green",
        "lightblue",
        "pink",
        "gold"]
        raam6=Tk()
        raam6.title("Ringid")
        tahvel6=Canvas(raam6,width=600,height=600,bg="white")
        x0=0
        y0=0
        x1=600
        y1=600
        p=5
        for i in range(55):
            x0+=p 
            y0+=p
            x1-=p 
            y1-=p 
            tahvel6.create_oval(x0,y0,x1,y1, fill=choice(colors))
            #sleep(1)
        tahvel6.grid()
        raam6.mainloop()
    elif num == 7:
        raam9 = Tk()
        raam9.title("Tahvel")
        tahvel = Canvas(raam9, width=350, height=500, background="white")
        tahvel.grid()

        tahvel.create_line(0, 250, 250, 250, width=500, fill="white")
        font1 = font.Font(font="Algerian 12")
        tahvel.create_text(50, 10, text="Valgusfoor", font=font1, anchor=NW)
        tahvel.create_line(150, 100, 200, 100, width=45, fill="red")
        tahvel.create_line(150, 150, 200, 150, width=45, fill="yellow")
        tahvel.create_line(150, 200, 200, 200, width=45, fill="green")
        tahvel.create_line(175, 230, 175, 450, width=8, fill="black")
        tahvel.create_line(80, 460, 260, 460, width=4, fill="black")
        tahvel.grid()
        raam9.mainloop()
    elif num == 8:
        raam91 = Tk()
        raam91.title("Tahvel")
        tahvel = Canvas(raam91, width=350, height=500, background="white")
        tahvel.grid()

        tahvel.create_line(0, 250, 250, 250, width=500, fill="white")
        font1 = font.Font(font="Algerian 12")
        tahvel.create_text(50, 10, text="Valgusfoor", font=font1, anchor=NW)
        tahvel.create_line(150, 100, 200, 100, width=45, fill="grey")
        tahvel.create_line(150, 150, 200, 150, width=45, fill="grey")
        tahvel.create_line(150, 200, 200, 200, width=45, fill="grey")
        tahvel.create_line(175, 230, 175, 450, width=8, fill="black")
        tahvel.create_line(80, 460, 260, 460, width=4, fill="black")
        tahvel.grid()
        raam91.mainloop()





aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")
var=IntVar() #StringVar()
r1=Radiobutton(aken,text="Флаг Богамских островов",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Эстонский флаг",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Флаг Индонезии",variable=var,value=3,command=valik)
r4=Radiobutton(aken,text="Квадраты",variable=var,value=4,command=valik)
r5=Radiobutton(aken,text="шахматы",variable=var,value=5,command=valik)
r6=Radiobutton(aken,text="круги",variable=var,value=6,command=valik)
r7=Radiobutton(aken,text="светофор",variable=var,value=7,command=valik)
r8=Radiobutton(aken,text="не рабочий светофор",variable=var,value=8,command=valik)
lbox=Listbox(aken,height=3,width=30) 


lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)
r5.grid(row=5,column=0)
r6.grid(row=6,column=0)
r7.grid(row=7,column=0)
r8.grid(row=8,column=0)
aken.mainloop()


#1 флаг
raam1 = Tk()
raam1.title("Tahvel")
tahvel1 = Canvas(raam1, 
                width=250, 
                height=150, 
                background="white")
tahvel1.create_rectangle(0,0, 250,150,fill="#4cacc2")
tahvel1.create_rectangle(0,50, 250,150,fill="yellow")
tahvel1.create_rectangle(0,100, 250,150,fill="#4cacc2")
tahvel1.create_polygon(0,0, 110,85, 0,150, fill="black")
tahvel1.grid()
raam1.mainloop()


#2 флаг
raam2 = Tk()
raam2.title("Tahvel")
tahvel2 = Canvas(raam2, 
                width=250, 
                height=150, 
                background="white")
tahvel2.create_rectangle(0,0, 250,150,fill="blue")
tahvel2.create_rectangle(0,50, 250,150,fill="black")
tahvel2.create_rectangle(0,100, 250,150,fill="white")
tahvel2.grid()
raam2.mainloop()


#3 флаг

raam3 = Tk()
raam3.title("Tahvel")
tahvel3 = Canvas(raam3, 
                width=250, 
                height=150, 
                background="white")
tahvel3.create_rectangle(0,0, 250,150,fill="red")
tahvel3.create_rectangle(0,73, 250,150,fill="white")
tahvel3.grid()
raam3.mainloop()
