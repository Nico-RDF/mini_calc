
import tkinter as tk
from tkinter import ttk

# ============================================================
#   DARK MODE STYLISCHER MINI‑RECHNER
# ============================================================

def calculate(op):
    try:
        a = float(entry.get())
        b = float(entry2.get())

        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            result.set("Fehler" if b == 0 else a / b)

    except ValueError:
        result.set("Ungültig")


# ============================================================
#   ROOT WINDOW (Dark Mode)
# ============================================================

root = tk.Tk()
root.title("Stylish Dark Calculator")
root.geometry("280x350")
root.configure(bg="#1e1e1e")  # Dark mode Hintergrund

# Styling
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Segoe UI", 14),
                padding=6,
                background="#2d2d2d",
                foreground="white")

style.map("TButton",
          background=[("active", "#3a3a3a")])

# Rahmen (kompakt wie Handy‑Taschenrechner)
main = tk.Frame(root, bg="#1e1e1e", padx=10, pady=10)
main.pack(expand=True)


# ============================================================
#   Eingabefelder (kompakt, dunkel)
# ============================================================

entry = tk.Entry(main, font=("Segoe UI", 18), width=10,
                 justify="right", bg="#111", fg="white",
                 insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

entry2 = tk.Entry(main, font=("Segoe UI", 18), width=10,
                  justify="right", bg="#111", fg="white",
                  insertbackground="white")
entry2.grid(row=1, column=0, columnspan=4, pady=5)

# Ergebnis
result = tk.StringVar()
result_label = tk.Label(main, textvariable=result, font=("Segoe UI", 18, "bold"),
                        bg="#222", fg="#00ff88", height=2)
result_label.grid(row=2, column=0, columnspan=4, sticky="we", pady=10)


# ============================================================
#   Buttons: Icons + Animation + kompakte Anordnung
# ============================================================

buttons = [
    ("＋", "+"),
    ("－", "-"),
    ("×", "*"),
    ("÷", "/"),
]

# Hover‑Effekte
def on_enter(e):
    e.widget["bg"] = "#444"

def on_leave(e):
    e.widget["bg"] = "#2d2d2d"


for i, (symbol, op) in enumerate(buttons):
    btn = tk.Button(main,
                    text=symbol,
                    font=("Segoe UI", 18),
                    bg="#2d2d2d",
                    fg="white",
                    activebackground="#3a3a3a",
                    command=lambda o=op: calculate(o))

    btn.grid(row=3, column=i, padx=4, pady=4, sticky="nsew")

    # Animation hinzufügen
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


# Tasten gleichmäßig machen
for i in range(4):
    main.grid_columnconfigure(i, weight=1)

root.mainloop()
