# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:41:25 2022

@author: richa
"""

import csv
import numpy
import tkinter
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Creating a figure to show all factor maps
fig = plt.figure(figsize=(10, 4))
fig_rows = 1
fig_columns = 3

# Creating the raster files (geology, transport, and population) from "csv" files as lists
with open("geology.csv", newline='') as f1:
    reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)
    geology = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        geology.append(rowlist)
    #print(geology)            # Verifying the "geology" raster


with open("transport.csv", newline='') as f2:
    reader = csv.reader(f2, quoting=csv.QUOTE_NONNUMERIC)
    transport = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        transport.append(rowlist)
    #print(transport)            # Verifying the "transport" raster


with open("population.csv", newline='') as f3:
    reader = csv.reader(f3, quoting=csv.QUOTE_NONNUMERIC)
    population = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        population.append(rowlist)
    #print(population)            # Verifying the "population" raster


# Ploting all maps:
# Adding the "geology" subplot at the 1st position
fig.add_subplot(fig_rows, fig_columns, 1)
plt.imshow(geology, cmap = "Greys")
plt.axis("off")
plt.title("Geology", fontweight = "bold")
#plt.colorbar(ticks = [255, 0], label = "Least suitable                             Most suitable")

# Adding the "transport" subplot at the 2nd position
fig.add_subplot(fig_rows, fig_columns, 2)
plt.imshow(transport, cmap = "Greys")
plt.axis("off")
plt.title("Transport", fontweight = "bold")
#plt.colorbar(ticks = [255, 0], label = "Least suitable                             Most suitable")

# Adding the "population" subplot at the 3rd position
fig.add_subplot(fig_rows, fig_columns, 3)
plt.imshow(population, cmap = "Greys")
plt.axis("off")
plt.title("Population", fontweight = "bold")
plt.colorbar(ticks = [255, 0], label = "Least suitable                             Most suitable")


# Building the main window and creating the layout
root = tkinter.Tk()
root.wm_title("Suitability analysis")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Creating the menu
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

# Assigning the weight of each factor from user's input
def assign_weights():
    
    def assign_values():
        global a, b, c
        a = geo.get()   # geology weight input
        b = tra.get()   # transport weight input
        c = pop.get()   # population weight input
        print("User's weights for Geology, Transport, and Population =", a, ",", b, ",", c)
    
    weight = tkinter.Tk()
    weight.geometry("300x300")
    weight.wm_title("Weighting")
    
    # Creating slider for Geology
    geo_label = tkinter.Label(weight, text = "Geology", fg = "dark blue", font = "bold")
    geo_label.place(x=12, y=10)
    geo = tkinter.Scale(weight, from_=0, to = 10, length = 200, tickinterval = 2, fg = "dark blue")
    geo.place(x=10, y=40)
    
    # Creating slider for Transport
    tra_label = tkinter.Label(weight, text = "Transport", fg = "dark blue", font = "bold")
    tra_label.place(x=109, y=10)
    tra = tkinter.Scale(weight, from_=0, to = 10, length = 200,  tickinterval = 2, fg = "dark blue")
    tra.place(x=110, y=40)
    
    # Creating slider for Population
    pop_label = tkinter.Label(weight, text = "Population", fg = "dark blue", font = "bold")
    pop_label.place(x=206, y=10)
    pop = tkinter.Scale(weight, from_=0, to = 10, length = 200,  tickinterval = 2,  fg = "dark blue")
    pop.place(x=210, y=40)
    
    # Buttons to assign weights
    Button1 = tkinter.Button(weight, text = 'Assign', fg = "dark blue", command = assign_values)
    Button1.place(x=70, y=260)
    Button2 = tkinter.Button(weight, text = 'OK', fg = "dark blue", command = weight.destroy)
    Button2.place(x=190, y=260)
    
    weight.mainloop()

# Creating the "Weights" menu, to assign the weights    
weight_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label = "Weights", menu = weight_menu)
weight_menu.add_command(label = "Assign weights", command = assign_weights)

#Adding a function to analyse and process the three factors
def suitability():
    
    # Converting the lists to arrays to easily calculating them to site suitability
    geology_array = numpy.array(geology)
    transport_array = numpy.array(transport)
    population_array = numpy.array(population)
    
    # Assigning the user weight inputs to the factors
    geology_weight = a
    transport_weight = b
    population_weight = c
         
    # Calculating the site location (as an array)
    suitable_site_array = geology_array*geology_weight + transport_array*transport_weight + population_array*population_weight
    
    # Finding the maximun value of the site location to change scale
    max_suitable_site_array = numpy.amax(suitable_site_array)
    print("Maximum value obtained from calculations =", round(max_suitable_site_array, 2))
     
    
    # Converting back and plotting the final array to a list and,
    # Changing the outcome to a 0-255 scale like the inputs
    global suitable_site
    suitable_site = []
    for row in suitable_site_array:
        rowlist = []
        for value in row:
            rowlist.append(value * 255 / max_suitable_site_array)
        suitable_site.append(rowlist)   
    
    # Confirming the maximun value of the site location to 255
    max_suitable_site = numpy.amax(suitable_site)
    print("Confirmed maximum rescaled value =", max_suitable_site)    
    
    # Plotting the final outcome
    plt.imshow(suitable_site, cmap = "Greys")
    plt.axis("off")
    plt.title("Suitable areas", fontweight="bold")
    plt.colorbar(ticks = [255, 0], label = "Least suitable                                           Most suitable")

    # Testing the outout using one input point
    print("Geology input value =", geology[400][200])
    print("Transport input value =", transport[400][200])
    print("Population input value =", population[400][200])
    print("Output value (example) =", round(suitable_site[400][200],1))

   
# Writing out the final output as a CSV file
def print_outcome():   
    f4 = open("Suitable areas.csv", "w", newline='') 
    writer = csv.writer(f4, delimiter=',')
    for row in suitable_site:
        writer.writerow(row)
    f4.close()

    
# Creating the "Model" menu
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Show suitability", command=suitability)
model_menu.add_command(label="Print outcome", command=print_outcome)

# Selecting and showing the top 10% of suitable areas (values higher than 230)
def top_10_percent():
    top_10 = []
    for row in suitable_site:
        rowlist = []
        for value in row:
            if value > 230:
                rowlist.append(value)
            else:
                rowlist.append(0)
        top_10.append(rowlist)   
      
    plt.imshow(top_10, cmap = "Blues")
    plt.axis("off")
    plt.title("Top 10% suitable", fontweight = "bold", color = "#00008B")
    plt.colorbar(ticks = [255, 0], label = "Least suitable                                           Most suitable")


# Selecting and showing the top 20% of suitable areas (values higher than 205)
def top_20_percent():
    top_20 = []
    for row in suitable_site:
        rowlist = []
        for value in row:
            if value > 205:
                rowlist.append(value)
            else:
                rowlist.append(0)
        top_20.append(rowlist)   
      
    plt.imshow(top_20, cmap = "Blues")
    plt.axis("off")
    plt.title("Top 20% suitable", fontweight = "bold", color = "#00008B")
    plt.colorbar(ticks = [255, 0], label = "Least suitable                                           Most suitable")

    
# Selecting and showing the top 10% of suitable areas (values higher than 180)
def top_30_percent():
    top_30 = []
    for row in suitable_site:
        rowlist = []
        for value in row:
            if value > 180:
                rowlist.append(value)
            else:
                rowlist.append(0)
        top_30.append(rowlist)   
      
    plt.imshow(top_30, cmap = "Blues")
    plt.axis("off")
    plt.title("Top 30% suitable", fontweight = "bold", color = "#00008B")
    plt.colorbar(ticks = [255, 0], label = "Least suitable                                           Most suitable")


# Creating the "Suitability" menu
suitability_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Suitability", menu=suitability_menu)
suitability_menu.add_command(label="Top 10%", command=top_10_percent)
suitability_menu.add_command(label="Top 20%", command=top_20_percent)
suitability_menu.add_command(label="Top 30%", command=top_30_percent)
suitability_menu.add_command(label="Back to 100%", command=suitability)

tkinter.mainloop()
