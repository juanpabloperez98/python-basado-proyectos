from tkinter import *
root = Tk()
miFrame = Frame()
miFrame.config(bg="red",width="200",height="200")
miFrame.pack()
miLabel = Label(miFrame, text = "Este es mi label")
miLabel.place(x=50,y=50)
root.mainloop()