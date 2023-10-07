from tkinter import *

root = Tk()
root.title('Color Changer')
root.geometry('400x400')
root.configure(background = 'coral1')

mode = 1
def changeColor():
    global mode 
    mode = mode % 4 + 1
    root.configure(background = f'coral{ mode }')

btnColor = Button(root, text = 'Change Color', command = lambda: changeColor())
btnColor.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()