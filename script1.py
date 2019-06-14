from tkinter import *

window = Tk()

def kg_2_weight():
    g1.delete(1.0,END)
    p1.delete(1.0,END)
    o1.delete(1.0,END)
    grams = float(e1_value.get())*1000
    lbs = float(e1_value.get())*2.20462
    oz = float(e1_value.get())*35.274
    g1.insert(END, grams)
    p1.insert(END, lbs)
    o1.insert(END, oz)

w1 = Label(window, text="KG")
w1.grid(row = 0, column = 0)

b1 = Button(window, text="Execute", command = kg_2_weight)
b1.grid(row= 0, column = 2)

e1_value = StringVar()

e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column = 1)

g_label = Label(window, text="Grams")
g_label.grid(row =1, column = 0)

g1=Text(window, height =1, width = 20)
g1.grid(row = 1 , column = 1)

p_label = Label(window, text="Lbs")
p_label.grid(row =1, column = 2)
p1=Text(window, height =1, width = 20)
p1.grid(row = 1 , column = 3)

o_label = Label(window, text="OZ")
o_label.grid(row =1, column = 4)
o1=Text(window, height =1, width = 20)
o1.grid(row = 1 , column = 5)

 
window.mainloop()

