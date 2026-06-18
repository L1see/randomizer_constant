import tkinter

import customtkinter
import random

file = open("data.txt", "r", encoding="utf-8")

line_count = 0
for line in file:
    line_count += 1

def button_callback():
    random_ideas()

def random_ideas():
    with open('data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        random_line = random.choice(lines)

        text_box.delete("0.0", "end")
        text_box.insert("0.0", random_line.strip())

def random_words():
    words = [
        'Хуйня',
        'Норм',
        "Отлично",
        "Иди нахуй"
    ]
    a = random.randint(0, len(words) - 1)
    result = words[a]
    text_box_1.delete("0.0", 'end')
    text_box_1.insert("0.0", result)
app = customtkinter.CTk()


app.title("Ну очень полезная программа")
app.geometry("500x500")

button = customtkinter.CTkButton(app, text="Жми для идеи!", command=button_callback)
app.grid_columnconfigure(0, weight=1)
button.grid(row=0, column=0, padx=20, pady=20)

text_box = customtkinter.CTkTextbox(app, width=400, height=150)
text_box.grid(row=1, column=0, padx=20, pady=(0, 20))

button = customtkinter.CTkButton(app, text="Оценка идеи от ИИ", command=random_words)
app.grid_columnconfigure(0, weight=1)
button.grid(row=2, column=0, padx=20, pady=20)

text_box_1 = customtkinter.CTkTextbox(app, width=400, height=150)
text_box_1.grid(row=3, column=0, padx=20, pady=(0, 20))

app.mainloop()