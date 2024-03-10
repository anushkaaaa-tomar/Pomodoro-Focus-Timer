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
timer_on = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_on)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_fun():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        timer.config(text="break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        timer.config(text="break", fg=GREEN)
    else:
        countdown(work_sec)
        timer.config(text="work", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_Sec = count % 60
    if count_Sec < 10:
        count_Sec = f"0{count_Sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_Sec}")
    if count > 0:
        global timer_on
        timer_on = window.after(1000, countdown, count-1)
    else:
        timer_fun()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔️"
        checkmarks.config(text=marks)


window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, background=YELLOW)


canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomato_ig = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_ig)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)

start_text = Button(text="Start", bg=YELLOW, highlightthickness=0, command=timer_fun)
start_text.grid(column=0, row=2)

reset_text = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_text.grid(column=2, row=2)

checkmarks = Label(bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)


window.mainloop()
# ---------------------------- UI SETUP ------------------------------- #





window.mainloop()
