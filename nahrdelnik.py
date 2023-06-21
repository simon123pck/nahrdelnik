import tkinter as tk
import random

w = 600
h = 500
colours = ["pink", "yellow", "blue", "green"]
count = 10
size = 45
move_list = []
proces_list = []
start = size
list_10 = []
def setup():
    global move_list
    for i in range(40):
        x = random.randrange(0, w - size)
        y = random.randrange(0, h - size*3)
        move_list.append(canvas.create_oval(x, y, x + size, y + size, fill=colours[i//10]))
    canvas.create_image(0, h - size-size//2, image=image, anchor=tk.NW)

def check_it(e):
    global proces_list, move_list, list_10
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in move_list:
        if len(proces_list) == 0 and len(list_10) < 10:
            proces_list.append(zoz[0])
            list_10.append(zoz[0])
            move_list.remove(zoz[0])
            print("stalo sa")
    move_it()

def move_it():
    global proces_list
    if len(proces_list) != 0:
        coord_ball = canvas.coords(proces_list[0])
        final_pos = (w-size//2,h-size//2)
        dx = w-coord_ball[2]
        dy = final_pos[1]-coord_ball[3]
        if dx>dy:
            dx = dx/dy
            dy = 1
        elif dx < dy:
            dy = dy / dx
            dx = 1
        canvas.move(proces_list[0],dx,dy)
        if coord_ball[2] == w:
            nit()
    #canvas.coords(proces_list[0])
    canvas.after(10,move_it)

def nit():
    global start, proces_list
    coord_ball = canvas.coords(proces_list[0])
    if coord_ball[0] > start:
        canvas.move(proces_list[0],-1,0)
        canvas.after(3,nit)
    else:
        start += size
        proces_list = []

win = tk.Tk()

canvas = tk.Canvas(win,width=w,height=h,bg="white")
canvas.bind("<Button-1>", check_it)
canvas.pack()

image = tk.PhotoImage(file="img.png")

setup()

win.mainloop()
