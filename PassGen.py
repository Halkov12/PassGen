import random
import tkinter as tk
from tkinter import messagebox, ttk


def generate_password():
    try:
        nums = int(entry_length.get())
        colvo = int(entry_count.get())
        uper = var_upper.get()
        specsimvol = var_special.get()

        if not (1 <= nums <= 100) or not (1 <= colvo <= 10):
            messagebox.showerror("Ошибка", "Введите корректные значения длины и количества паролей!")
            return

        str_all = '1234567890qwertyuiopasdfghjklzxcvbnm'
        str_spec = '.,:;!_*-+()/#¤%&'
        str_up = str_all.upper()

        if uper and specsimvol:
            str_chars = str_all + str_spec + str_up
        elif uper:
            str_chars = str_all + str_up
        elif specsimvol:
            str_chars = str_all + str_spec
        else:
            str_chars = str_all

        ls = list(str_chars)
        random.shuffle(ls)

        passwords = ["".join(random.choice(ls) for _ in range(nums)) for _ in range(colvo)]
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(passwords))
        output_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения!")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    root.update()
    messagebox.showinfo("Скопировано", "Пароль(и) скопированы в буфер обмена!")


def save_to_file():
    with open("passwords.txt", "w") as f:
        f.write(output_text.get("1.0", tk.END).strip())
    messagebox.showinfo("Сохранено", "Пароли сохранены в файл passwords.txt!")


# Создание окна
root = tk.Tk()
root.title("PassGen")
root.geometry("400x400")
root.configure(bg="#2E2E2E")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#444", foreground="white", font=("Arial", 10))
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Arial", 10))
style.configure("TCheckbutton", background="#2E2E2E", foreground="white", font=("Arial", 10))

# Ввод длины пароля
ttk.Label(root, text="Длина пароля (1-100):").pack()
entry_length = ttk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, length=200)
entry_length.pack()

# Ввод количества паролей
ttk.Label(root, text="Количество паролей (1-10):").pack()
entry_count = ttk.Entry(root)
entry_count.pack()

# Флажки для выбора
var_upper = tk.BooleanVar()
var_special = tk.BooleanVar()
ttk.Checkbutton(root, text="Заглавные буквы", variable=var_upper).pack()
ttk.Checkbutton(root, text="Спецсимволы", variable=var_special).pack()

# Кнопка генерации
btn_generate = ttk.Button(root, text="Сгенерировать", command=generate_password)
btn_generate.pack()

# Поле вывода паролей
output_text = tk.Text(root, height=10, state=tk.DISABLED, bg="#444", fg="white")
output_text.pack()

# Кнопки для копирования и сохранения
btn_copy = ttk.Button(root, text="Копировать", command=copy_to_clipboard)
btn_copy.pack()
btn_save = ttk.Button(root, text="Сохранить в файл", command=save_to_file)
btn_save.pack()

# Запуск приложения
root.mainloop()