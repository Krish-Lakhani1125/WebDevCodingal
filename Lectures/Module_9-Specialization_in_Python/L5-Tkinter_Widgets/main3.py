from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

#function to open new (top level) window
def topwin():
    #Setting up top window
    top = Toplevel()
    top.geometry("100x100")
    top.title("toplevel")
    #Adding a label widget to top window
    l2 = Label(top, text ='this is toplevel window')
    l2.pack()

    top.mainloop()

#Adding a label and button widget to Root (main) window
l=Label(root, text = "This is root window")
btn = Button(root, text ="Click here to open another window", command=topwin)
#Arranging Widgets
l.pack()
btn.pack()
root.mainloop()