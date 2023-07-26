import tkinter as tk
import hashlib

def save_credentials():
    login = entry_login.get()
    password = entry_password.get()


    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    with open('credentials.txt', 'w') as file:
        file.write(f"Логин: {login}\n")
        file.write(f"Хэшированный пароль: {hashed_password}")


    entry_login.delete(0, tk.END)
    entry_password.delete(0, tk.END)


window = tk.Tk()
window.title("Сохранение логина и пароля")
window.geometry("300x200")


label_login = tk.Label(window, text="Логин:")
label_login.pack()
entry_login = tk.Entry(window)
entry_login.pack()


label_password = tk.Label(window, text="Пароль:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()


button_save = tk.Button(window, text="Сохранить", command=save_credentials)
button_save.pack()


window.mainloop()