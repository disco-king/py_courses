from tkinter import *

win_side = 600
rect_side = win_side / 10

def get_rect(x, y):
    x = x // rect_side
    y = y // rect_side
    return (x, y)

def print_rect(event):
    ret = get_rect(event.x, event.y)
    print(ret)

root = Tk()

c = Canvas(root, width=win_side, height=win_side, bg='white')
c.pack()
 
for i in range(1,10):
    step = i*rect_side
    c.create_line(step, 0, step, win_side)
    c.create_line(0, step, win_side, step)

root.bind("<Button-1>", print_rect)

root.mainloop()