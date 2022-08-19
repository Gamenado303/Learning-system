import tkinter as tk
import globals as g
import main_menu as mm

PADX = 20
font_size = 20

def back(browse_frame):
    browse_frame.destroy()
    mm.display_main_menu()

def display_back_button(browse_frame):
    title_frame = tk.Frame(master = browse_frame, bg = g.BACKGROUND, height = 30)
    title_frame.pack(fill = tk.X, side = "top")
    back_button = tk.Button(master = title_frame, 
                            text = "Back", 
                            font = (g.FONT, font_size), 
                            relief = tk.RAISED, 
                            width = 10,
                            command = lambda: back(browse_frame))
    back_button.pack(side = "right", pady = 20, padx = PADX)
    g.highlight_button(back_button, font_size)

def open_set(set_name):
    with open(f"{set_name.get()}.txt", "r") as f:
        pass

def set_list(browse_frame):
    list_frame = tk.Frame(master = browse_frame, bg = g.BACKGROUND)
    list_frame.pack(fill = tk.X, side = "top")
    with open(g.SAVED_SETS, "r") as f:
        name = f.readline().strip()
        get_set = tk.Button(master = list_frame, 
                        text = name, 
                        font = (g.FONT, font_size), 
                        relief = tk.RAISED, 
                        width = 10,
                        command = lambda: open_set(name))
        get_set.pack(side = "top", pady = 20, padx = PADX)
        g.highlight_button(get_set, font_size)

def display_browse_set():
    browse_frame = tk.Frame(master = g.main_window, bg = g.BACKGROUND)
    browse_frame.pack(fill = tk.BOTH, expand=True)
    display_back_button(browse_frame)
    set_list(browse_frame)