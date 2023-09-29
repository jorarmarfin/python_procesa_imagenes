from tkinter import *

def redimensionar():
    print('hola')
 
def crear_label():
    v_y = v_y + 10
    Label(frame,text='Label creada').place(x=50,y=v_y)
 


root = Tk()
root.title('Procesador de imagenes')
root.resizable(0,0)
frame = Frame(root)
frame.pack()
frame.config(width=1024,height=700)


Label(frame,text='Redimenciona las imagnes y extrae el rostro').place(x=10,y=10)

Button(frame,text='Redimensionar',command=crear_label).place(x=10,y=30)

root.mainloop()