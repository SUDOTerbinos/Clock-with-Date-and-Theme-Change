import tkinter as tk
from time import strftime
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x300")

is_dark_mode = True

def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        root.configure(bg="white")
        label_time.config(fg="black", bg="white")
        label_date.config(fg="black", bg="white")
        theme_button.config(text="Dark Mode", bg="lightgray")
        is_dark_mode = False
    else:
        root.configure(bg="black")
        label_time.config(fg="cyan", bg="black")
        label_date.config(fg="cyan", bg="black")
        theme_button.config(text="Light Mode", bg="gray")
        is_dark_mode = True

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label_time.config(text=current_time)
    current_date = datetime.now().strftime('%A, %d %B %Y')
    label_date.config(text=current_date)
    label_time.after(1000, update_time)

label_time = tk.Label(root, text="", font=("Helvetica", 48), fg="cyan", bg="black")
label_time.pack(pady=10)

label_date = tk.Label(root, text="", font=("Helvetica", 20), fg="cyan", bg="black")
label_date.pack(pady=10)

theme_button = tk.Button(root, text="Light Mode", font=("Helvetica", 14), bg="gray", fg="white", command=toggle_theme)
theme_button.pack(pady=20)

update_time()
root.mainloop()
