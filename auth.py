import tkinter as tk
import configs as cfg
import json
import os
from tkinter import messagebox as msg
import webbrowser

#ввод урл
#self.uLabel = tk.Label(okno, text="Введите url (с .com)")
#   self.uLabel.pack(pady=5)
#
#   self.uEntry = tk.Entry(okno, width=50)
#   self.uEntry.pack(pady=5)
#   self.uEntry.insert(0, "https://www.google.com")
#
#   def open_in_browser(self):
#   url = self.uEntry.get()
#   if not url.startswith(("http://", "https://")):
#   url = "https://" + url
#   try:
#   webbrowser.open(url)
#   except Exception as e:
#   msg.showerror("Ошибка", f"Не удалось открыть ссылку: {e}")


# Путь к файлу с пользователями
DB_FILE = "base.json"


def load_users():
    """Загружает данные пользователей из JSON-файла."""
    if not os.path.exists(DB_FILE):
        # Если файла нет, создаем его с тестовым пользователем
        default_data = {"users": [{"username": "ronalda", "password": "stayak"}]}
        with open(DB_FILE, "w") as f:
            json.dump(default_data, f, indent=4)
        return default_data
    else:
        with open(DB_FILE, "r") as f:
            return json.load(f)


def save_users(data):
    """Безопасно сохраняет данные пользователей в JSON-файл."""
    try:
        # Проверка структуры данных
        if not isinstance(data, dict) or "users" not in data:
            raise ValueError("Некорректная структура данных")

        # Создаём временный файл для безопасной записи
        temp_file = DB_FILE + ".tmp"

        with open(temp_file, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        # Заменяем старый файл новым только после успешной записи
        if os.path.exists(temp_file):
            if os.path.exists(DB_FILE):
                os.remove(DB_FILE)
            os.rename(temp_file, DB_FILE)
            return True

    except PermissionError:
        msg.showerror("Ошибка", "Нет прав для записи файла")
    except IOError as e:
        msg.showerror("Ошибка", f"Ошибка записи: {str(e)}")
    except Exception as e:
        msg.showerror("Ошибка", f"Непредвиденная ошибка: {str(e)}")

    return False


def checkpass():
    username = personLogin.get()
    password = personPassword.get()

    data = load_users()
    users = data["users"]

    if not username and not password:
        msg.showerror("Внимание", "Логин и пароль не могут быть пустыми!")
        return

    # Проверяем, есть ли пользователь в базе
    for user in users:
        if user["username"] == username and user["password"] == password:
            msg.showinfo("Успех!", f"Добро пожаловать, {username}!")
            authh.destroy()
            open_browser()
            return

    msg.showerror("Ошибка", "Неверный логин или пароль!")


def regnewuser():
    username = personLogin.get()
    password = personPassword.get()

    if not username or not password:
        msg.showerror("Внимание", "Логин и/или пароль не может(-гут) быть пустым(-ыми)")
        return

    data = load_users()
    users = data["users"]

    for user in users:
        if user["username"] == username or user["password"] == password:
            msg.showerror("Внимание", "Этот логин или пароль уже занят!")
            return

    new_user = {"username": username, "password": password}
    users.append(new_user)
    save_users(data)

    msg.showinfo("Успех!", "Регистрация прошла успешно!")


def open_browser():
    browser = tk.Tk()
    browser.title(cfg.TITLEE)
    browser.geometry(f"{cfg.WIDTHH}x{cfg.HEIGHTT}")
    browser.iconbitmap(cfg.ICO)

    # Поле ввода URL
    tk.Label(browser, text="Введите url: ").pack(pady=5)
    url_entry = tk.Entry(browser, width=30)
    url_entry.pack(pady=5)
    url_entry.insert(0, "https://")

    tk.Button(browser, text="Открыть в браузере", command=lambda: openinbrowser(url_entry.get())).pack(pady=10)

    browser.mainloop()

def openinbrowser(url):
    if not isinstance(url, str) or not url.strip():
        msg.showerror("Ошибка", "URL должен быть непустой строкой")
        return

    url = url.strip()

    try:
        webbrowser.open(url, new=2)  # new=2 открывает в новой вкладке
    except webbrowser.Error as e:
        msg.showerror("Ошибка", f"Не удалось открыть браузер: {e}")
    except Exception as e:
        msg.showerror("Ошибка", f"Непредвиденная ошибка: {e}")



# создание окна авторизации
authh = tk.Tk()
authh.title(cfg.TITLE)
authh.geometry(f"{cfg.WIDTH}x{cfg.HEIGHT}")
authh.iconbitmap(cfg.ICO)

#текст + кнопки
tk.Label(authh, text="Войдите в аккаунт").pack()
tk.Label(authh, text="Логин:").pack(pady=5)  # pady = 5 - отступ по шкале x

personLogin = tk.Entry(authh, width=15)
personLogin.pack()

tk.Label(authh, text="Пароль: ").pack()

personPassword = tk.Entry(authh, width=15, show="*")
personPassword.pack()

tk.Button(authh, text="Войти", command=checkpass).pack()
tk.Button(authh, text="Зарегистрироватся", command=regnewuser).pack(pady=3)

authh.mainloop()
