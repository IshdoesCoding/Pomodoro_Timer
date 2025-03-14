from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#fff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    Timer_title.config(text = "Timer")
    check_text.config(text= "")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps %2 != 0:
        count_down(work_sec)
        Timer_title.config(text = "Work", fg = GREEN )
    elif reps %2 == 0:
        count_down(short_break_min)
        Timer_title.config(text = "Break", fg = PINK )
    elif reps % 8 == 0:
        count_down(long_break_min)
        Timer_title.config(text = " Long Break", fg = RED )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1 )
    else:
        start_timer()
        marks = '✓'
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += '✓'
        check_text.config(text = marks)






# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady= 50, bg = YELLOW)


#canvas
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness= 0)
pomodoro_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = pomodoro_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))

canvas.grid(column = 1, row = 1)



#labels

Timer_title = Label(text = "Timer", font = (FONT_NAME, 40, "bold" ), fg = GREEN, highlightthickness=0, bg= YELLOW)
Timer_title.grid(column = 1, row = 0)

check_text = Label(font = (FONT_NAME, 10, "bold"), fg = GREEN, bg = YELLOW, highlightthickness=0)
check_text.grid(column = 1, row = 3)

#Button
start_button = Button(text ="Start", width= 5, bg = WHITE, highlightthickness=0, command = start_timer)
start_button.grid(column = 0, row = 2)

Reset_button = Button(text ="Reset", width= 5, bg = WHITE, highlightthickness=0, command = reset_timer)
Reset_button.grid(column = 2, row = 2)


window.mainloop()