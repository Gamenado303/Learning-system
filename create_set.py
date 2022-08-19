import tkinter as tk
import globals as g

PADX = 10
PADX1 = 50
PADY = 5
LABEL_FONT_SIZE = 18
TEXTBOX_FONT_SIZE = 20
ENTRY_WIDTH = 50
cards = []
set_name = []

def close(e):
    e.destroy()

def display_title(new_window):
    font_size = 20
    title_frame = tk.Frame(master = new_window, bg = g.BACKGROUND)
    title_frame.pack(fill = tk.X, side = "top")
    title = tk.Label(master = title_frame,
                        text = "Title:",
                        bg = g.BACKGROUND,
                        fg = "white",
                        font = (g.FONT, 20))
    title.pack(side = "left", padx = PADX, pady = 20)
    input_title = tk.Entry(master = title_frame,
                        font = (g.FONT, 24),
                        width = 35)
    input_title.pack(side = "left", pady = 20)
    set_name.append(input_title)
    close_button = tk.Button(master = title_frame, 
                        text = "Close", 
                        font = (g.FONT, font_size), 
                        relief = tk.RAISED, 
                        width = 10,
                        command = lambda: close(new_window))
    close_button.pack(side = "right", pady = 20, padx = PADX)
    g.highlight_button(close_button, font_size)
    save_button = tk.Button(master = title_frame, 
                        text = "Save", 
                        font = (g.FONT, font_size), 
                        relief = tk.RAISED, 
                        width = 10,
                        command = lambda: save_set())
    save_button.pack(side = "right", pady = 20, padx = PADX)
    g.highlight_button(save_button, font_size)

def display_card(new_window):
    new_card = tk.Frame(master = new_window, bg = g.BACKGROUND)
    new_card.pack(fill = tk.X)
    question_label_frame = tk.Frame(master = new_card, bg = g.BACKGROUND)
    question_label_frame.pack(fill = tk.X, pady = PADY)
    question_label = tk.Label(master = question_label_frame,
                        text = f"Question {len(cards)}",
                        bg = g.BACKGROUND,
                        fg = "white",
                        font = (g.FONT, LABEL_FONT_SIZE, "underline"))
    question_label.pack(side = "left", padx = PADX1)
    new_question = tk.Frame(master = new_card, bg = g.BACKGROUND)
    new_question.pack(fill = tk.X, pady = PADY)
    question = tk.Entry(master = new_question,
                        font = (g.FONT, TEXTBOX_FONT_SIZE),
                        width = ENTRY_WIDTH)
    question.pack(side = "left", padx = PADX1)
    answer_label_frame = tk.Frame(master = new_card, bg = g.BACKGROUND)
    answer_label_frame.pack(fill = tk.X, pady = PADY)
    answer_label = tk.Label(master = answer_label_frame,
                        text = "Answer",
                        bg = g.BACKGROUND,
                        fg = "white",
                        font = (g.FONT, LABEL_FONT_SIZE, "underline"))
    answer_label.pack(side = "left", padx = PADX1)
    new_answer = tk.Frame(master = new_card, bg = g.BACKGROUND)
    new_answer.pack(fill = tk.X, pady = PADY)
    answer = tk.Entry(master = new_answer,
                        font = (g.FONT, TEXTBOX_FONT_SIZE),
                        width = ENTRY_WIDTH)
    answer.pack(side = "left", padx = PADX1)
    return [question, answer]

def add_card(new_window, frame):
    if frame != None:
        frame.destroy()
        frame = tk.Frame(master = new_window, bg = g.BACKGROUND, height = 30)
        frame.pack(fill = tk.X)
    
    cards.append("")
    cards[-1] = display_card(new_window)
    frame = tk.Frame(master = new_window, bg = g.BACKGROUND)
    frame.pack(fill = tk.X, pady = PADY)
    
    add_set_button = tk.Button(master = frame, 
                        text = "Add new card", 
                        font = (g.FONT, 16), 
                        relief = tk.RAISED, 
                        command = lambda: add_card(new_window, frame))
    add_set_button.pack(side = "left", pady = 10, padx = PADX1)
    g.highlight_button(add_set_button, 16)

def set_up_scroll(new_window):
    container = tk.Frame(master = new_window, bg = g.BACKGROUND)
    canvas = tk.Canvas(master = container, bg = g.BACKGROUND, highlightbackground = g.BACKGROUND)
    scrollbar = tk.Scrollbar(master = container, orient="vertical", command = canvas.yview, bg = g.BACKGROUND)
    scrollable_frame = tk.Frame(master = canvas, bg = g.BACKGROUND)
    scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )
    canvas.create_window((0, 0), window = scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand = scrollbar.set)
    container.pack(fill = tk.BOTH, expand = True)
    canvas.pack(side="left", fill = tk.BOTH, expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    return scrollable_frame

def save_set():
    with open(g.SAVED_SETS, "a") as f:
        f.write(set_name[-1].get())
        f.write("\n")
    with open(f"{set_name[-1].get()}.txt", "w") as f:
        for i in cards:
            f.write(i[0].get())
            f.write("\n")
            f.write(i[1].get())
            f.write("\n")

def display_new_set():
    new_window = tk.Tk()
    new_window.title("New set")
    new_window.geometry("600x360")
    new_window.configure(bg = g.BACKGROUND)
    display_title(new_window)
    scrollable_frame = set_up_scroll(new_window)
    add_card(scrollable_frame, None)
    
    