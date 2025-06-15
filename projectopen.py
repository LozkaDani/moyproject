# PLAN
# 1. меню - открыватель проектов (моих кншн)
# 2. Мини игра "Крутите барабан!" - вобшэм угадываем пукофке
# 3. Скачать обои клэш рояль... ой скачать видео с ЮТУБА!!!!! - ну вы поняли
# итог - я маладец

import tkinter as tk
import subprocess as sp
from tkinter import StringVar

infoOL = "Открыватель ссылок\n это программа открывающая вашу ссылку в основном браузере.\n *при создании использовалась нейросеть*. Библиотеки в коде: tkinter, webbrowser, os и json"
infoMT = "Математический тест чтобы проверить свои знания в математике. \n Библиотеки: random и tkinter"
infoSB = "Мини-игра 'Крутите барабан!'\n Вам нужно угадать слово по буквам.\n Библиотеки: random и tkinter "

menu = tk.Tk()
menu.title("Меню выбора проекта")
menu.geometry("400x440")
menu.iconbitmap("iconi.ico")

lbl_1 = tk.Label(menu, text="Выберите проект для запуска: ")
lbl_1.grid(row=0, column=1)

btn_1 = tk.Button(menu, text="Открыватель ссылок", width=18, height=7, command=lambda: infoadd(1))
btn_1.grid(row=1, column=0)

btn_2 = tk.Button(menu, text="Математический тест", width=18, height=7, command=lambda: infoadd(2))
btn_2.grid(row=3, column=0)

btn_3 = tk.Button(menu, text="Крутите Барабан!", width=18, height=7, command=lambda: infoadd(3))
btn_3.grid(row=5, column=0)

tk.Label(menu, text="", height=2).grid(row=4, column=0)
tk.Label(menu, text="", height=2).grid(row=2,column=0)
tk.Label(menu, text="", width=0).grid(row=2, column=1)
info_l = tk.Label(menu, text="")
info_l.grid(row=1, column=1)

vibor = StringVar()
vibor.set("Выберите проект")
vars = ["Открыватель ссылок", "Математический тест", "Крутите Барабан!"]
btn_4 = tk.OptionMenu(menu, vibor, *vars, command= lambda x: openProject())
btn_4.grid(row=3, column=1)

def infoadd(wpo):
    if wpo == 1:
        info_l["text"] = infoOL
        menu.geometry("680x440")
        n = 1

    if wpo == 2:
        info_l["text"] = infoMT
        menu.geometry("510x440")
        n = 2

    if wpo == 3:
        info_l["text"] = infoSB
        menu.geometry("400x440")
        n = 3
    return

def openProject():
    uvibor = vibor.get()

    if uvibor == "Открыватель ссылок":
        sp.run(["python", "auth.py"])
        exit()

    if uvibor == "Математический тест":
        sp.run(["python", "mathtest.py"])
        exit()

    if uvibor == "Крутите Барабан!":
        sp.run(["python", "game.py"])
        exit()
    return

menu.mainloop()