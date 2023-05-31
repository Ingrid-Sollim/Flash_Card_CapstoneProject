from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

#TODO 2: Read the data from csv file
try:
    data = pd.read_csv("data/french_words_updated.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
    #print(data_dict)

#TODO 3: ramdom pair of words
pair = choice(data_dict)
# print(pair)
# alter_title = pair['French']
# print(alter_title)

def random_french_word():
    '''Show a random french word from the data file.'''
    global pair
    global flip_timer
    #window.after_cancel(flip_timer) #so every time we click in one of the buttons, it is going to invalidade the timer. And the start counting in the landing card
    pair = choice(data_dict)
    #print(pair)
    alter_title = pair['French']
    canvas_white.itemconfig(canvas_image, image=card_white)
    canvas_white.itemconfig(white_title,text="French", fill="Black")
    canvas_white.itemconfig(white_word,text=alter_title, fill="Black")
    flip_timer = window.after(3000, english_translate)

def ok_button():
    random_french_word()
    data_dict.remove(pair)
    new_df=pd.DataFrame(data_dict)
    new_df.to_csv("data/french_words_updated.csv", index=False)
    #pair_index = data_dict.index(pair)
    #print(pair_index)


def english_translate():
    '''Show the english translation from the french card'''
    canvas_white.itemconfig(canvas_image,image=card_green)
    canvas_white.itemconfig(white_title, text="English",fill="white")
    translator = pair['English']
    canvas_white.itemconfig(white_word, text=translator,fill="white")
    print(translator)

#TODO 1: Create the user interface
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)


#Create the white canvas
canvas_white = Canvas(width=800, height=526)
#Front card
card_white = PhotoImage(file="images/card_front.png")
#Back card
card_green = PhotoImage(file="images/card_back.png")
#Create the image inside the canvas_white
canvas_image = canvas_white.create_image(400, 263, image=card_white)
white_title = canvas_white.create_text(400,150,text="",font=("Ariel",40,"italic"),tags="title")
white_word = canvas_white.create_text(400,263,text="",font=("Ariel",60,"bold"),tags="words")
canvas_white.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_white.grid(row=0,column=0,columnspan=2)

#Create the buttons
nok_image = PhotoImage(file="images/wrong.png")
notok_button = Button(image=nok_image,highlightthickness=0,command=random_french_word)
#notok_button.config(padx=50, pady=50)
notok_button.grid(row=1,column=0)

ok_image = PhotoImage(file="images/right.png")
ok_button = Button(image=ok_image,highlightthickness=0,command=ok_button)
#notok_button.config(padx=50, pady=50)
ok_button.grid(row=1,column=1)

random_french_word()


flip_timer = window.after(3000,english_translate)
window.mainloop()