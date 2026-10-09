import tkinter as tk
from tkinter import ttk, messagebox


def calc_discount(user_age: int, is_user_active: bool) -> float:
    discount_mul = 1.0

    if user_age < 18:
        discount_mul *= 0.9  # 10% discount for minors

    if not is_user_active:
        discount_mul *= 0.8  # 20% discount for inactive users

    return discount_mul


def on_calculate():
    try:
        price = float(price_entry.get().replace(",", "."))
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Цена и возраст должны быть числами.")
        return

    if price < 0 or age < 0:
        messagebox.showerror("Ошибка", "Цена и возраст не могут быть отрицательными.")
        return

    mul = calc_discount(age, active_var.get())
    final_price = price * mul
    discount_percent = (1 - mul) * 100

    result_var.set(
        f"Множитель: {mul:.2f}\n"
        f"Скидка: {discount_percent:.0f}%\n"
        f"Итоговая цена: {final_price:,.2f} ₽".replace(",", " ")
    )


root = tk.Tk()
root.title("Калькулятор скидки")
root.resizable(False, False)

frame = ttk.Frame(root, padding=16)
frame.grid()

ttk.Label(frame, text="Цена (₽):").grid(row=0, column=0, sticky="w", pady=4)
price_entry = ttk.Entry(frame, width=20)
price_entry.insert(0, "28000")
price_entry.grid(row=0, column=1, pady=4)

ttk.Label(frame, text="Возраст:").grid(row=1, column=0, sticky="w", pady=4)
age_entry = ttk.Entry(frame, width=20)
age_entry.insert(0, "20")
age_entry.grid(row=1, column=1, pady=4)

active_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Пользователь активен", variable=active_var).grid(
    row=2, column=0, columnspan=2, sticky="w", pady=4
)

ttk.Button(frame, text="Рассчитать", command=on_calculate).grid(
    row=3, column=0, columnspan=2, pady=8
)

result_var = tk.StringVar(value="Введите данные и нажмите «Рассчитать»")
ttk.Label(frame, textvariable=result_var, justify="left").grid(
    row=4, column=0, columnspan=2, sticky="w"
)

root.bind("<Return>", lambda e: on_calculate())

root.mainloop()
