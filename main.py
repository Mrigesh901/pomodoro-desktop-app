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


def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(countdown_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        timer_label.config(text="Study", fg=GREEN)
    elif reps == 8:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = int(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(countdown_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        study_sessions = int(reps/2)
        for _ in range(study_sessions):
            marks += "✔"
            check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=300, height=250)
window.config(padx=110, pady=50, bg=YELLOW)
window.title("Pomodoro")

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_label = Label(text="", font=(FONT_NAME, 20, "bold"), highlightthickness=0)
check_label.config(fg=GREEN)
check_label.grid(column=1, row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
countdown_text = canvas.create_text(100, 124, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
