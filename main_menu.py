import tkinter as tk
import create_set as cs
import globals as g
import browse as b

BUTTON_WIDTH = 20


def browse_set_button(e):
    e.destroy()
    b.display_browse_set()

def create_set_button():
    cs.display_new_set()

def close_button():
    g.main_window.destroy()

def display_main_menu():
    main_menu = tk.Frame(master = g.main_window, bg = g.BACKGROUND)
    main_menu.pack(fill = tk.BOTH)
    logo = tk.Label(master = main_menu, image = g.LOGO)
    logo.pack(side = "top", pady = 40)

    browse = tk.Button(master = main_menu, 
                        text = "Browse Sets", 
                        font = (g.FONT, g.FONT_SIZE), 
                        relief = tk.RAISED, 
                        width = BUTTON_WIDTH,
                        command = lambda: browse_set_button(main_menu))
    browse.pack(side = "top", pady = 10)
    g.highlight_button(browse)
    create = tk.Button(master = main_menu, 
                        text = "Create Set", 
                        font = (g.FONT, g.FONT_SIZE), 
                        relief = tk.RAISED, 
                        width = BUTTON_WIDTH, 
                        command = lambda: create_set_button())
    create.pack(side = "top", pady = 10)
    g.highlight_button(create)
    stats = tk.Button(master = main_menu, 
                        text = "View Stats", 
                        font = (g.FONT, g.FONT_SIZE), 
                        relief = tk.RAISED, 
                        width = BUTTON_WIDTH)
    stats.pack(side = "top", pady = 10)
    g.highlight_button(stats)
    close = tk.Button(master = main_menu, 
                        text = "Close", 
                        font = (g.FONT, g.FONT_SIZE), 
                        relief = tk.RAISED, 
                        width = BUTTON_WIDTH,
                        command= lambda: close_button())
    close.pack(side = "top", pady = 10)
    g.highlight_button(close)
