from tkinter import *
import gomoku

win_side = 600
rect_side = win_side // 10

def get_rect(x, y):
    x = x // rect_side
    y = y // rect_side
    return [x, y]

def create_rect(cds):
    c.create_rectangle(cds[0] * rect_side + 10,
                    cds[1] * rect_side + 10,
                    (cds[0] + 1) * rect_side - 10,
                    (cds[1] + 1) * rect_side - 10,
                    width=3, activefill="gray")

def draw_move(cds, move):
    top_x = cds[0] * rect_side + 10
    top_y = cds[1] * rect_side + 10
    bot_x = (cds[0] + 1) * rect_side - 10
    bot_y = (cds[1] + 1) * rect_side - 10

    if move:
        c.create_line(top_x, top_y,
                        bot_x, bot_y,
                        width=3)
        c.create_line(top_x, top_y + 40,
                        bot_x, bot_y - 40,
                        width=3)
    else:
        c.create_oval(top_x, top_y,
                        bot_x, bot_y,
                        width=3)

def place_x(event, field):
    ret = get_rect(event.x, event.y)

    move = True
    ret = gomoku.make_move(field, move, ret[0], ret[1])
    if not ret:
        return
    draw_move(ret, human_first)
    move = not move
    ret = gomoku.make_move(field, move)
    draw_move(ret, not human_first)
    print(ret)

root = Tk()

c = Canvas(root, width=win_side, height=win_side, bg='white')
c.pack()

for i in range(1,10):
    step = i*rect_side
    c.create_line(step, 0, step, win_side)
    c.create_line(0, step, win_side, step)

field = gomoku.field_init()

human_first = BooleanVar()
human_first = True

if not human_first:
    ret = gomoku.make_move(field, False)
    draw_move(ret, not human_first)

root.bind("<Button-1>", lambda e, 
            f=field: place_x(e, f))

root.mainloop()