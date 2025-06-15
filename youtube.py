from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
import tkinter as tk
from tkinter import messagebox


def download_video():
    url = t_1.get().strip()
    quality = vibor.get()

    if not url or url == "Ссылка на видео":
        messagebox.showerror("Ошибка", "Введите ссылку на видео!")
        return

    try:
        video = YouTube(url)
        stream = video.streams.filter(res=quality).first()

        if stream:
            stream.download()
            messagebox.showinfo("Успех", f"Видео '{video.title}' скачано в {quality}!")
        else:
            messagebox.showerror("Ошибка", f"Качество {quality} недоступно!")

    except RegexMatchError:
        messagebox.showerror("Ошибка", "Некорректная ссылка на YouTube!")
    except VideoUnavailable:
        messagebox.showerror("Ошибка", "Видео недоступно или удалено!")


# GUI
okno = tk.Tk()
okno.title("YouTube Downloader")
okno.geometry("300x200")

tk.Label(okno, text="Ссылка на видео:").pack()
t_1 = tk.Entry(okno, width=30)
t_1.pack()
t_1.insert(0, "https://www.youtube.com/watch?v=...")

tk.Label(okno, text="Качество:").pack()
vibor = tk.StringVar(okno)
vibor.set("720p")  # Значение по умолчанию
qualities = ["144p", "240p", "360p", "480p", "720p", "1080p"]
tk.OptionMenu(okno, vibor, *qualities).pack()

tk.Button(okno, text="Скачать", command=download_video).pack(pady=10)

okno.mainloop()
