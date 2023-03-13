#imports
from tkinter import * 
import pandas
import random


#-------------------------------- SELECT WORD ------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")
selected_word = {}


def known_word():
    data_dict.remove(selected_word)
    data_dict_file = pandas.DataFrame(data_dict)
    data_dict_file.to_csv("data/words_to_learn.csv", index=False) 
    select_word()


def select_word():
    global selected_word, card_delay
    window.after_cancel(card_delay)
    selected_word = random.choice(data_dict)
    canvas.itemconfig(language_id, text="French", fill="black")
    canvas.itemconfig(word_id, text=selected_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    card_delay = window.after(3000, change_card)

def change_card():
    canvas.itemconfig(language_id, text="English", fill="white")
    canvas.itemconfig(word_id, text=selected_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)



#-------------------------------- UI ------------------------------------#

#consts
BACKGROUND_COLOR = "#B1DDC6"

#window
window = Tk()
window.config(width=1200, height=700, bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title(string="Flashy")
card_delay = window.after(3000, change_card)

#card

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

language_id = canvas.create_text(400, 100, text="", font=("arial", 40, 'italic'))
word_id = canvas.create_text(400, 250, text="", font=("arial", 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)


#buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=select_word)
wrong_button.grid(column=0, row=1)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

select_word()


window.mainloop()
