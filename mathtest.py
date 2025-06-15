import tkinter as tk
import random as r

titles = ["Алексей, вам кто-то звонит, возьмите трубку.", "окак", "ГОЙДААА", "1488", "lin gan guli guli guli"]


num1 = 30
num2 = 10
op = "+"

operators = ["+", "-", "*", "/"]

bali = 0


def randomnum():
    global num1, num2, op

    while True:
        num1 = r.randint(1, 100)
        num2 = r.randint(1, 100)
        op = r.choice(operators)
        if op == "*":
            break
        elif num1 >= num2:
            break

        else:
            continue

    l_1["text"] = f"{num1}{op}{num2}"
    t_1.delete(0, tk.END)
    return num1, num2, op

def check():
    global bali
    try:
        user_answer = int(t_1.get())
    except ValueError:
        t_1.delete(0, tk.END)
        t_1.insert(0, "Введите число")
        return bali

    correct = None

    if op == "+":
        correct = (num1 + num2 == user_answer)
    elif op == "-":
        correct = (num1 - num2 == user_answer)
    elif op == "*":
        correct = (num1 * num2 == user_answer)
    elif op == "/":
        correct = (num1 // num2 == user_answer) or (num1 / num2 == user_answer)

    if correct:
        bali += 1
        l_1["text"] = f"Правильно! +1 балл\nВсего баллов: {bali}"
        return bali
    else:
        l_1["text"] = f"Неправильно! Правильный ответ: {eval(f'{num1}{op}{num2}')}"

    return bali


test = tk.Tk()
test.title(r.choice(titles))
test.geometry("220x150")
test.iconbitmap("icon.ico")

l_1 = tk.Label(test, text="Нажми Рандомайзер чтобы начать")
l_1.pack()

l_4 = tk.Label(test, text="Ответ")
l_4.pack()

t_1 = tk.Entry(test, width=10)
t_1.pack()

b_1 = tk.Button(test, text="Проверить...", width=15, height=1, command=lambda: check())
b_1.pack()

b_2 = tk.Button(test, text="Рандомайзер", width=15, height=1, command=lambda: randomnum())
b_2.pack()

test.mainloop()