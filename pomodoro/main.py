from tkinter import *
from tkinter import simpledialog
import math
from turtle import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ""
timer = None


# ---------------------------- Setter ------------------------------- #


def setter(minute, short_break, long_break):
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    if minute is not None:
        WORK_MIN = int(minute)
    if short_break is not None:
        SHORT_BREAK_MIN = int(short_break)
    if long_break is not None:
        LONG_BREAK_MIN = int(long_break)

    print(WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN)


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer, reps
    reps = 0
    window.after_cancel(timer)
    Timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps == 8:
        Timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
    elif reps % 2 == 0:
        Timer_label.config(text="Break", fg=PINK)
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        count_down(short_break_sec)
    else:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        Timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count = int(count)
    global reps
    count_min = math.floor(int(count) / 60)
    count_sec = int(count) % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        global check_mark
        if reps % 2 == 0:
            check_mark += "✔️"

        start_timer()
        check_label.config(text=f"{check_mark}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=10, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

Timer_label = Label()
Timer_label.config(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW)
Timer_label.grid(row=0, column=1)

check_label = Label(fg=GREEN, font=(FONT_NAME, 16, "bold"), bg=YELLOW)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


# -------------------------------------- attempt ------------------------------------------ #
# screen = Screen()
# screen.withdraw()
# minutes = screen.textinput(title="set working minutes", prompt="working minutes")
# short_minutes = screen.textinput(title="set short break minutes", prompt="short break")
# long_minutes = screen.textinput(title="set long break minutes", prompt="long break")
# screen.bye()
# setter(minutes, short_minutes, long_minutes)
root = Tk()
root.withdraw()

minutes = simpledialog.askstring("Input", "set working minutes", parent=root)
short_minutes = simpledialog.askstring("Input", "set short break minutes", parent=root)
long_minutes = simpledialog.askstring("Input", "set long break minutes", parent=root)

setter(minutes, short_minutes, long_minutes)

# -------------------------------------- attempt ------------------------------------------ #


window.mainloop()







