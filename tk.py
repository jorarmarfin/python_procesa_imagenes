from tkinter import *
root = Tk()
root.title('Procesador de imagenes')
root.resizable(0,0)
frame = Frame(root)
frame.pack()
frame.config(width=1024,height=700)


imagen = PhotoImage(file="assets/logo-uni.png")

Label(frame,image=imagen).place(x=30,y=30)
Label(frame,text='Redimenciona las imagnes y extrae el rostro').place(x=10,y=10)


root.mainloop()