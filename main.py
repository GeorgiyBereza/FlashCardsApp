from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

"""If it's user's first time - app works with original file, else it uses csv without known words"""
try:
    csv_french_words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    csv_french_words = pandas.read_csv("./data/french_words.csv")

french_words = csv_french_words.to_dict(orient="records")
current_card = random.choice(french_words)

def generate_random_word():
    global current_card
    current_card = random.choice(french_words)
    card.itemconfig(card_image,image=front_img)
    card.itemconfig(card_title,text="French", fill="black")
    card.itemconfig(card_word,text=current_card["French"], fill="black")


def flip_card():
    """This command shows the translation"""
    card.itemconfig(card_title,text="English", fill="white")
    card.itemconfig(card_word,text=current_card["English"], fill="white")
    card.itemconfig(card_image,image=back_img)


def right():
    """This command implies that user knows this word, so it's deleted from the dict"""
    french_words.remove(current_card)
    data = pandas.DataFrame(french_words)
    data.to_csv("data/words_to_learn.csv",index=False)
    generate_random_word()


def wrong():
    """This command implies that user doesn't know this word, so it stays in the dict"""
    generate_random_word()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards App")
window.config(height=826, width=1100,padx=50,pady=50,bg=BACKGROUND_COLOR)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

card = Canvas(height=526, width=800, highlightthickness=0, background=BACKGROUND_COLOR)
card_image = card.create_image(400,263,image=front_img)
card_title = card.create_text(400, 150, text="",font=("Ariel",40,"italic"))
card_word = card.create_text(400, 263, text="",font=("Ariel",60,"bold"))

card.grid(row=0,column=0,columnspan=3)

button_wrong = Button(image=wrong_img, command=wrong)
button_wrong.grid(row=1,column=0)
button_check = Button(text="Check", font=("Ariel",40,"bold"), command=flip_card)
button_check.grid(row=1,column=1)
button_right = Button(image=right_img, command=right)
button_right.grid(row=1,column=2)

generate_random_word()
window.mainloop()