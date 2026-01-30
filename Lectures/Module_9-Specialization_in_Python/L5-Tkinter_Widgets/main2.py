from tkinter import *
from tkinter import messagebox

#Setup tkinter window
root = Tk()
root.geometry("200x200")

#function for displaying warning msg
#This will be called once the bttn is clicked
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found.")

#Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()