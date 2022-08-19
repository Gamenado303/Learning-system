import tkinter as tk
from PIL import ImageTk, Image

BACKGROUND = "#424242"
FONT = "SimSun"
FONT_SIZE = 16
SAVED_SETS = "_saved_sets.txt"

def highlight_button(button, font_size = FONT_SIZE):
    def on_enter(e):
        e.widget["background"] = "#a3a29e"
        e.widget["font"] = (FONT, font_size, "underline")

    def on_leave(e):
        e.widget["background"] = 'SystemButtonFace'
        e.widget["font"] = (FONT, font_size)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

main_window = tk.Tk()
main_window.geometry("600x360")
main_window.title("Quizlet 2.0")    
main_window.configure(bg = BACKGROUND)

LOGO = ImageTk.PhotoImage(Image.open("symbol.jpg"))



