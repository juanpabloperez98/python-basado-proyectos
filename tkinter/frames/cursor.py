from tkinter import *
root = Tk()
root.config(bg="blue",bd=10,relief="groove")
root.geometry("300x300")
miFrame = Frame()
miFrame.config(bg="red",width="100",height="100",bd=10,relief="groove",cursor="pirate")
miFrame.pack()
root.mainloop()