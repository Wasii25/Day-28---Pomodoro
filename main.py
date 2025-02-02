from tkinter import *

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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%2 != 0:
        count_down(work_sec)
        title.config(text="Work", fg=PINK)
    elif reps%8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg=YELLOW)

    else:
        count_down(short_break_sec)
        title.config(text="Short Break", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1 )
    else:
        start_timer()
        if reps%2 == 0:
            check.config(text="✅")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 50), fg=RED, bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(highlightthickness=0, bg=YELLOW, fg=RED)
check.grid(column=1, row=2)

window.mainloop()
