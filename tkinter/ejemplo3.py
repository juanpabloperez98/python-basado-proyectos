from tkinter import *

""" Labels """

root = Tk()
frame = Frame(root,width="500",height="400")
frame.config(bg="blue",bd=35,relief="groove")
frame.pack()

imagen = PhotoImage(file = "proyecto.png")
# Label 
# label = Label(frame,text="Hola mundo", fg="red", font =("Comic Sans MS",18))
label = Label(frame, image = imagen)
label.place(x=0,y=0)
root.mainloop()