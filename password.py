import tkinter as tk
from tkinter import messagebox
import random

alfabe = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
semboller = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
             '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def generate_password():
    try:
        kullanıcıalfabe = int(entry_harf.get())
        kullanıcırakamlar = int(entry_rakam.get())
        kullanıcısemboller = int(entry_sembol.get())

        password_list = []

        for i in range(kullanıcıalfabe):
            password_list.append(random.choice(alfabe))
        for i in range(kullanıcırakamlar):
            password_list.append(str(random.choice(rakamlar)))
        for i in range(kullanıcısemboller):
            password_list.append(random.choice(semboller))

        random.shuffle(password_list)

        password = "".join(password_list)
        result_label.config(text=f"Şifreniz: {password}")

    except ValueError:
        messagebox.showerror("Hata","Lütfen Tüm Alanlara Geçerli Bir Sayı Girin.")


root = tk.Tk()
root.title("Şifre Üretici")
root.geometry("400x275")

tk.Label(root,text="Kaç Tane Harf İstiyorsunuz?").pack()
entry_harf=tk.Entry(root)
entry_harf.pack()

tk.Label(root,text="Kaç Tane Rakam İstiyorsunuz?").pack()
entry_rakam=tk.Entry(root)
entry_rakam.pack()

tk.Label(root,text="Kaç Tane Sembol İstiyorsunuz?").pack()
entry_sembol=tk.Entry(root)
entry_sembol.pack()

tk.Button(root, text="Şifre Üret",command=generate_password).pack(pady=10)

result_label=tk.Label(root,text="")
result_label.pack()

root.mainloop()
