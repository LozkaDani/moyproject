import random as r
import tkinter as tk

words = ["academy", "python", "it", "ai", "game", "code"]
word = r.choice(words)
guessed = ["_"] * len(word)

def game():
    letter = t_1.get().strip().lower()
    if "".join(guessed) == word:
        l_2["text"] = "Вы выиграли!"
        return
    if letter == "":
        l_4["text"] = "Буква не может быть пробелом!"
        return
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
        l_2.config(text=" ".join(guessed))
        l_4["text"] = ""
    else:
        l_4["text"] = "Этой буквы нет в слове!"

    t_1.delete(0, 'end')

ogame = tk.Tk()
ogame.title("Мини-игра Крутите барабан!")
ogame.geometry("300x300")
ogame.iconbitmap("icon.ico")

l_1 = tk.Label(ogame, text="Угаданные буквы:")

l_2 = tk.Label(ogame, text="".join(guessed))

l_3 = tk.Label(ogame, text="Введите букву (англ)")

l_4 = tk.Label(ogame, text="")

t_1 = tk.Entry(ogame, width=5)

b_1 = tk.Button(ogame, text="Проверить букву", width=15, height=2, command=lambda: game())

podskazka = tk.Label(ogame, text="")

l_1.pack()
l_2.pack()
l_3.pack()
t_1.pack()
b_1.pack()
l_4.pack()
podskazka.pack()

words = ["academy", "python", "it", "ai", "game", "code"]

if word == "academy":
    podskazka["text"] = "То где мы учимся (7 букв)"
elif word == "python":
    podskazka["text"] = "То что мы проходили (6 букв)"
elif word == "it":
    podskazka["text"] = "Расшифровка на русском Информационные Технологии(2 буквы)"
elif word == "ai":
    podskazka["text"] = "Умный но не Эйнштейн(2 буквы)"
elif word == "code":
    podskazka["text"] = "То что мы писали в это блоке(4 буквы)"
elif word == "game":
    podskazka["text"] = "Мини .... (4 буквы)"

ogame.mainloop()
