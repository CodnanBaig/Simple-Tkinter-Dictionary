import tkinter as tk

import requests


def dictionary():
    word = word_input.get()
    url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    response = url.json()

    definition = response[0]["meanings"][0]["definitions"][0]["definition"]
    examples = response[0]["meanings"][0]["definitions"][0]["example"]

    result.config(text=f"Definition: '{definition}'")
    example.config(text=f"Example: '{examples}'")


window = tk.Tk()
window.title("Python Eng Dictionary")
window.minsize(width=500, height=80)
window.config(pady=20)

label = tk.Label(text="Type in a word to search it's meaning", font=("Ariel", 12, "bold"))
label.grid(column=0, row=0)
label.config(padx=100, pady=10)

word_input = tk.Entry(width=20)
word_input.grid(row=1)

button = tk.Button(text="Search", command=dictionary)
button.grid(row=3)

result = tk.Label(text="", font=("Ariel", 12, "italic"))
result.grid(row=4)
result.config(padx=50, pady=25)

example = tk.Label(text="",  font=("Ariel", 12, "italic"))
example.grid(row=5)
example.config(padx=50, pady=10)

window.mainloop()
