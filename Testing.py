# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:10:01 2022

@author: richa
"""

import csv
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot



from tkinter import *
root = Tk()

root.geometry('250x200+250+200')
Label(root, text="Position 1").place(x=10, y=5)
Label(root, text="Position 2").place(x=50, y=40)
Label(root, text="Position 3").place(x=75, y=80)

root.mainloop()





'''
with open('geology.csv', newline='') as f1:
    reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)
    geology = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        geology.append(rowlist)
        
with open('transport.csv', newline='') as f2:
    reader = csv.reader(f2, quoting=csv.QUOTE_NONNUMERIC)
    transport = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        transport.append(rowlist)
'''



'''
fig, ax = matplotlib.pyplot.subplots()
matplotlib.pyplot.axis('off')
cax = ax.imshow(geology, cmap = 'Greys')
ax.set_title("Geology")
cbar = fig.colorbar(cax, ticks = [255, 0])
cbar.ax.set_yticklabels(["Most suitable", "Least suitable"])
'''



'''
#matplotlib.pyplot.ax.tick_params(labelsize = 8)
#matplotlib.pyplot.ax.set_title('Suitability', fontsize = 8)


matplotlib.pyplot.imshow(geology, cmap = 'Greys')
#matplotlib.pyplot.imshow(transport, cmap = 'Blues', alpha = 0.5)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("Geology")
matplotlib.pyplot.colorbar(ticks = [255, 0], label = "Least suitable                                           Most suitable")

'''





'''
with open('suitable site.csv', newline='') as f1:
    reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)
    site = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        site.append(rowlist)

matplotlib.pyplot.imshow(site)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("Site")

print(max(value))


top_10 = []
for row in site:
    rowlist = []
    for value in row:
        if value > 230:
            rowlist.append(value)
        else:
            rowlist.append(0)
    top_10.append(rowlist)   
  
matplotlib.pyplot.imshow(top_10)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("Top 10% suitable")
'''

'''
from tkinter import *


# Obainting input
def assign_values():
    print(geo.get(), tra.get(), pop.get())

weight = Tk()
geo_label = Label(weight, text = "Geology weight")
geo_label.pack()
geo = Scale(weight, from_=0, to = 10, length = 200, tickinterval = 2, orient = HORIZONTAL)
geo.pack()

tra_label = Label(weight, text = "Transport weight")
tra_label.pack()
tra = Scale(weight, from_=0, to = 10, length = 200,  tickinterval = 2, orient = HORIZONTAL)
tra.pack()

pop_label = Label(weight, text = "Population weight")
pop_label.pack()
pop = Scale(weight, from_=0, to = 10, length = 200,  tickinterval = 2, orient = HORIZONTAL)
pop.pack()

Button(weight, text = 'Assign weights', command = assign_values).pack()

mainloop()

'''''

''''
root = tkinter.Tk()
geo = tkinter.Scale(root, from_=0, to = 10)
geo.pack()
tra = tkinter.Scale(root, from_=0, to = 10)
tra.pack()
pop = tkinter.Scale(root, from_=0, to = 10)
pop.pack()


tkinter.mainloop()


'''







'''
#SCROLLBAR

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcomand = scrollbar.set)
for line in range(5):
    weight.insert(END, "Value = " + str(line))
    
mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

mainloop()
'''


'''
geo = 3

print(geo)


root_geo = tkinter.Tk()
root_geo.wm_title("From 0 to 1")

geo_frame = tkinter.Canvas(root_geo, width=150, height=1)
geo_frame.pack()

def assign():
    global geo
    geo = float(textbox.get())
   
def clear():
    textbox.delete(0,10)

textbox = tkinter.Entry(root_geo, justify="center", width=5)
textbox.pack()

clear_button = tkinter.Button(root_geo, text = "Clear",command = clear)
assign_button = tkinter.Button(root_geo, text = "Assign", command = assign)
close_button = tkinter.Button(root_geo, text = "Close", command = root_geo.destroy)

clear_button.pack()
assign_button.pack()
close_button.pack()

root_geo.mainloop()

'''


'''
root_geo = tkinter.Tk()
root_geo.wm_title("Geology weight")
geo_frame = tkinter.Canvas(root_geo, width=200, height=50)
geo_frame.pack()
geo_frame.create_rectangle(0, 0, 200, 50, fill="blue")

tkinter.mainloop()

'''



'''
a = [[1,2],[2,3],[3,4]]
b = [[2,3],[3,4],[4,5]]
c = [[3,4],[4,5],[5,6]]


# From list to array
a1 = numpy.array(a)
b1 = numpy.array(b)
c1 = numpy.array(c)



# Operations as arrays

d1 = (a1*0.63) + (b1*0.11) + (c1*0.26)




# from array to list
d = []
for row in d1:
    rowlist = []
    for value in row:
        rowlist.append(value)
    d.append(rowlist)




print(a)
print(b)
print(c)
print(d)


print(a1)
print(b1)
print(c1)



# Plotting
fig = matplotlib.pyplot.figure(figsize=(10, 4))
fig_rows = 1
fig_columns = 4


fig.add_subplot(fig_rows, fig_columns, 1)
matplotlib.pyplot.imshow(a)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("a")

fig.add_subplot(fig_rows, fig_columns, 2)
matplotlib.pyplot.imshow(b)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("b")

fig.add_subplot(fig_rows, fig_columns, 3)
matplotlib.pyplot.imshow(c)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("c")

fig.add_subplot(fig_rows, fig_columns, 4)
matplotlib.pyplot.imshow(d)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.title("d")


'''


'''
# Building the main window and creating the layout
root = tkinter.Tk()

root.wm_title("Agent-based model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Creating the menu and associating it to the "run" function
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()

'''





