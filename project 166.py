from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Working on Canvas Using Functions")
root.geometry("600x600")

canvas=Canvas(root, width = 590, height = 490, bg ="white",highlightbackground="lightgray")
canvas.pack()

color_label=Label(root, text="choose color:")
color_label.place(relx=0.6,rely=0.9, anchor = CENTER)

fill_color = ["green","red","blue","yellow"]

color_dropdown = ttk.Combobox(root,state="read only", values=fill_color, width= 10)
color_dropdown.place(relx=0.8,rely=0.9, anchor = CENTER)

startx=Label(root,text="startx")
startx.place(relx=0.1,rely=0.85,anchor = CENTER)

coordinate_values= [10,50,100,200,250,300,400,500]

sx = ttk.Combobox(root,state="readonly", values = coordinate_values, width = 10)
sx.place(relx=0.2,rely=0.85, anchor = CENTER)

starty=Label(root,text="starty")
starty.place(relx=0.3,rely=0.85,anchor = CENTER)

sy = ttk.Combobox(root,state="readonly", values = coordinate_values, width = 10)
sy.place(relx=0.4,rely=0.85, anchor = CENTER)

endx=Label(root,text="endx")
endx.place(relx=0.5,rely=0.85,anchor = CENTER)

endx = ttk.Combobox(root,state="readonly", values = coordinate_values, width = 10)
endx.place(relx=0.6,rely=0.85, anchor = CENTER)

endy=Label(root,text="endy")
endy.place(relx=0.7,rely=0.85,anchor = CENTER)

endy = ttk.Combobox(root,state="readonly", values = coordinate_values, width = 10)
endy.place(relx=0.8,rely=0.85, anchor = CENTER)

def circle(event):
    oldx = sx.get()
    oldy = sy.get()
    newx = endx.get()
    newy = endy.get()
    keypress = 'c'
    draw(keypress,oldx,oldy,newx,newy)

def rectangle(event):
    oldx = sx.get()
    oldy = sy.get()
    newx = endx.get()
    newy = endy.get()
    keypress = 'r'
    draw(keypress,oldx,oldy,newx,newy)

def line(event):
    oldx = sx.get()
    oldy = sy.get()
    newx = endx.get()
    newy = endy.get()
    keypress = 'l'
    draw(keypress,oldx,oldy,newx,newy)

def draw(keypress,oldx,oldy,newx,newy):
    fill_color = color_dropdown.get()
    if keypress=="c":
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,width = 3, fill=fill_color)
    if keypress=="r":
        draw_rectangle=canvas.create_rectangle(oldx,oldy,newx,newy,width = 3, fill=fill_color)
    if keypress=="l":
        draw_line=canvas.create_line(oldx,oldy,newx,newy,width = 3, fill=fill_color)

root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)

root.mainloop()