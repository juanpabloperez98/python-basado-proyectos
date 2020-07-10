from tkinter import *
""" Frames """
raiz = Tk()
raiz.config(bg="blue")
miFrame = Frame()
# miFrame.pack(side = "right",anchor ="n")
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="650", height="350")

miFrame.config(bd=35)
# miFrame.config(relief="groove")
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")


raiz.mainloop()