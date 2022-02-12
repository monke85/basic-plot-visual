from tkinter import *
import matplotlib
import matplotlib.pyplot as plt

def printtext():
    global x1
    global y1
    global x2
    global y2
    string = x1.get()
    string2 = y1.get()  
    string3 = x2.get()
    string4 = y2.get()
    plt.plot([float(string), float(string3)], [float(string2), float(string4)])
    plt.show()

def on_closing():
    window.destroy()

window = Tk()

x1 = Entry(window)
x1.pack()
x1.focus_set()
y1 = Entry(window)
y1.pack()
y1.focus_set()
x2 = Entry(window)
x2.pack()
x2.focus_set()
y2 = Entry(window)
y2.pack()
y2.focus_set()

b = Button(window,text='okay',command=printtext)
b.pack(side='bottom')
window.mainloop()


window.title('Visual')
window.geometry('800x600')
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()