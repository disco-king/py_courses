from tkinter import *
import gomoku
import time

win_side = 600
rect_side = win_side // 10

def get_rect(x, y):
    x = x // rect_side
    y = y // rect_side
    return [x, y]

def exit_win():
    root.destroy()

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

def finish_game(data, figure):
    x = data[0]
    y = data[1]
    direct = data[3]
    if figure:
        move = human_first
    else:
        move = not human_first
    for i in range(data[2]):
        c.create_rectangle(x * rect_side,
                            y * rect_side,
                            (x + 1) * rect_side,
                            (y + 1) * rect_side,
                            fill="red")
        draw_move((x, y), move)
        x += direct[0]
        y += direct[1]


def move_check(field, move, ret):
    ret = gomoku.make_move(field, move, ret[0], ret[1])
    if not ret:
        return 0
    draw_move(ret, human_first if move else not human_first)
    if ret[2]:
        finish_game(ret[3], move)
        return 1
    return 2


def next_move(event, field):
    ret = get_rect(event.x, event.y)

    result = move_check(field, True, ret)
    if result == 0:
        return
    if result == 1:
        game_over_prompt("Computer won!\nPlay again?")
    elif move_check(field, False, ret) == 1:
        game_over_prompt("Human won!\nPlay again?")


def init_window():
    for i in range(1,10):
        step = i*rect_side
        c.create_line(step, 0, step, win_side)
        c.create_line(0, step, win_side, step)

    global field
    field = gomoku.field_init()
    global human_first
    human_first = True

    root.attributes("-topmost", False)
    first_prompt()
    root.attributes("-topmost", True)

    root.bind("<Button-1>", lambda e, 
                f=field: next_move(e, f))

    if not human_first:
        ret = gomoku.make_move(field, False)
        draw_move(ret, not human_first)


def get_prompt(ptext, b1_text, b2_text, blst):
    prompt = Toplevel(root)
    prompt.geometry("200x100+310+350")
    prompt.resizable(False, False)
    prompt.overrideredirect(True)
    prompt.attributes("-topmost", True)

    Label(prompt, text=ptext, font="Arial 12").pack(side=TOP, pady=10)
    blst[0] = Button(prompt, text=b1_text, width=9)
    blst[1] = Button(prompt, text=b2_text, width=9)
    blst[0].pack(side=LEFT, padx=15)
    blst[1].pack(side=RIGHT, padx=15)

    return prompt


def game_over_prompt(prompt_text):
    blst = [0, 0]

    prompt = get_prompt(prompt_text, "Yes", "No", blst)

    def decide(event, yes):
        if yes:
            c.delete("all")
            init_window()
            prompt.quit()
            prompt.destroy()
        else:
            prompt.quit()
            prompt.destroy()
            root.destroy()

    blst[0].bind("<Button-1>", lambda e, 
                val=True: decide(e, val))
    blst[1].bind("<Button-1>", lambda e, 
                val=False: decide(e, val))
    prompt.mainloop()


def first_prompt():
    blst = [0, 0]

    prompt = get_prompt("Who plays first?", "Human", "Computer", blst)

    def set_first(event, val):
        global human_first
        human_first = val
        prompt.quit()
        prompt.destroy()

    blst[0].bind("<Button-1>", lambda e, 
                val=True: set_first(e, val))
    blst[1].bind("<Button-1>", lambda e, 
                val=False: set_first(e, val))
    prompt.mainloop()


root = Tk()
root.title("XOBot")
root.resizable(False, False)
root.geometry("+100+100")

c = Canvas(root, width=win_side, height=win_side, bg='white')
c.pack()

field = list()
human_first = bool()
game_over = BooleanVar()

init_window()


root.mainloop()