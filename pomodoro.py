from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, timer_text="00:00")
    my_tittle.config(text="Timer", fg=PINK)
    checkmark.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global rep
    rep += 1
    work_set = WORK_MIN * 60
    short_break_set = SHORT_BREAK_MIN * 60
    long_break_set = LONG_BREAK_MIN * 60
    while rep <= 6:
        if rep % 8 == 0:
            count_down(long_break_set)
            my_tittle.config(text="Long Break", fg=PINK)
        elif rep % 2 == 0:
            count_down(short_break_set)
            my_tittle.config(text="Short Break", fg=GREEN)
        else:
            count_down(work_set)
            my_tittle.config(text="Work Set", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # utilizar el floor para sacar solo los minutos restantes, sin redondear
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    # utilizar el modulo para sacar solo el restante, el segundo
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    # configurar el canvas directamente para cambiar la variable donde se encuentra nuestro timer
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # 1000 seria el segundo, la formula que va a llamar, la variable count restandole 1 para que sea descendiente
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        mark = ""
        # para que se ejecute cada dos veces
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            mark += "🗸"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Configure the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Create a canvas to import a image, highlightthickness es el borde de la canva
canvas = Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
# The image pass to a variable
photo = PhotoImage(file="tomato.png")
# Add the image to the canvas
canvas.create_image(105, 120, image=photo)
timer_text = canvas.create_text(105, 140, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

# Label for tittle in the window and for the checkmark
my_tittle = Label()
my_tittle.config(text="Timer", font=("Calisto MT", 30, "bold"), fg=PINK, background=YELLOW)
my_tittle.grid(column=1, row=0)
checkmark = Label()
checkmark.config(font=("Calisto MT", 30, "bold"), fg=PINK, background=YELLOW)
checkmark.grid(column=1, row=3)
# Add button to start and reset the tomato
start_buttons = Button(command=start_time, text="Start", font=("Calisto MT", 10), bg=GREEN, activebackground=YELLOW,
                       highlightthickness=0)
start_buttons.grid(column=0, row=2)
reset_button = Button(text="Reset", font=("Calisto MT", 10), bg=GREEN, activebackground=YELLOW, highlightthickness=0,
                      command=reset_time)
reset_button.grid(column=2, row=2)

window.mainloop()
