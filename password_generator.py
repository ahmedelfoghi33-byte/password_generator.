import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import math
import os

# Password Generator
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/<>~"

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    if length < 8:
        messagebox.showwarning(
            "Weak Password",
            "For better security, use at least 8 characters."
        )
        return

    characters = string.ascii_lowercase

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += SYMBOLS

    if not characters:
        messagebox.showerror(
            "Error",
            "Please select at least one character type."
        )
        return

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    password_var.set(password)
    update_strength()


def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "Nothing to copy",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    copy_button.config(text="✓ Copied!")
    root.after(1500, lambda: copy_button.config(text="Copy"))


def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="•")
        show_button.config(text="Show")
    else:
        password_entry.config(show="")
        show_button.config(text="Hide")


def calculate_entropy(password):
    if not password:
        return 0

    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in SYMBOLS for c in password):
        pool += len(SYMBOLS)

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)


def update_strength(*args):
    password = password_var.get()

    entropy = calculate_entropy(password)

    if not password:
        strength_label.config(
            text="Strength: —"
        )
        strength_bar["value"] = 0
        return

    if entropy < 40:
        strength = "Very Weak"
        value = 20

    elif entropy < 60:
        strength = "Weak"
        value = 40

    elif entropy < 80:
        strength = "Good"
        value = 65

    elif entropy < 100:
        strength = "Strong"
        value = 85

    else:
        strength = "Very Strong"
        value = 100

    strength_label.config(
        text=f"Strength: {strength}   |   Entropy: {entropy:.1f} bits"
    )

    strength_bar["value"] = value


def save_password():
    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "Nothing to save",
            "Generate a password first."
        )
        return

    file_path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "generated_password.txt"
    )

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(password)

        messagebox.showinfo(
            "Saved",
            f"Password saved to:\n{file_path}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not save password:\n{e}"
        )



# Window

root = tk.Tk()

root.title(" Password Generator")
root.geometry("600x650")
root.resizable(False, False)

root.configure(bg="#111827")


# Variables

password_var = tk.StringVar()

length_var = tk.StringVar(value="20")

uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


# Styles
style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass

style.configure(
    "TProgressbar",
    thickness=12
)


# =========================
# Header
# =========================

title = tk.Label(
    root,
    text=" Secure Password Generator by ahmed",
    font=("Segoe UI", 22, "bold"),
    bg="#111827",
    fg="white"
)

title.pack(pady=(30, 5))


subtitle = tk.Label(
    root,
    text="Generate strong and secure passwords",
    font=("Segoe UI", 11),
    bg="#111827",
    fg="#9CA3AF"
)

subtitle.pack(pady=(0, 25))


# =========================
# Password box
# =========================

password_frame = tk.Frame(
    root,
    bg="#1F2937"
)

password_frame.pack(
    padx=40,
    fill="x"
)


password_entry = tk.Entry(
    password_frame,
    textvariable=password_var,
    font=("Consolas", 18),
    bg="#1F2937",
    fg="white",
    insertbackground="white",
    relief="flat",
    show="•"
)

password_entry.pack(
    side="left",
    padx=15,
    pady=18,
    fill="x",
    expand=True
)


show_button = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password,
    bg="#374151",
    fg="white",
    activebackground="#4B5563",
    activeforeground="white",
    relief="flat",
    padx=12
)

show_button.pack(
    side="right",
    padx=10
)


# =========================
# Strength
# =========================

strength_label = tk.Label(
    root,
    text="Strength: —",
    font=("Segoe UI", 10, "bold"),
    bg="#111827",
    fg="#D1D5DB"
)

strength_label.pack(
    pady=(20, 8)
)


strength_bar = ttk.Progressbar(
    root,
    
    orient="horizontal",
    length=500,
    mode="determinate",
    maximum=100
)

strength_bar.pack()


# =========================
# Options
# =========================

options_frame = tk.Frame(
    root,
    bg="#142039"
)

options_frame.pack(
    pady=25
)


length_label = tk.Label(
    options_frame,
    text="Password Length:",
    font=("Segoe UI", 11),
    bg="#134FCE",
    fg="white"
)

length_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=8
)


length_spinbox = tk.Spinbox(
    options_frame,
    from_=8,
    to=128,
    textvariable=length_var,
    width=8,
    font=("Segoe UI", 11),
    bg="#2F3633",
    fg="white",
    buttonbackground="#374151"
)

length_spinbox.grid(
    row=0,
    column=1,
    padx=10
)


# Checkboxes

uppercase_check = tk.Checkbutton(
    options_frame,
    text="Uppercase A-Z",
    variable=uppercase_var,
    font=("Segoe UI", 10),
    bg="#111827",
    fg="white",
    selectcolor="#1F2937",
    activebackground="#111827",
    activeforeground="white"
)

uppercase_check.grid(
    row=1,
    column=0,
    sticky="w",
    pady=5
)


numbers_check = tk.Checkbutton(
    options_frame,
    text="Numbers 0-9",
    variable=numbers_var,
    font=("Segoe UI", 10),
    bg="#111827",
    fg="white",
    selectcolor="#1F2937",
    activebackground="#111827",
    activeforeground="white"
)

numbers_check.grid(
    row=1,
    column=1,
    sticky="w",
    pady=5
)


symbols_check = tk.Checkbutton(
    options_frame,
    text="Symbols !@#$",
    variable=symbols_var,
    font=("Segoe UI", 10),
    bg="#111827",
    fg="white",
    selectcolor="#1F2937",
    activebackground="#111827",
    activeforeground="white"
)

symbols_check.grid(
    row=2,
    column=0,
    sticky="w",
    pady=5
)


# =========================
# Buttons
# =========================

generate_button = tk.Button(
    root,
    text="🔄 Generate Password",
    command=generate_password,
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=12
)

generate_button.pack(
    pady=(5, 12)
)


buttons_frame = tk.Frame(
    root,
    bg="#111827"
)

buttons_frame.pack()


copy_button = tk.Button(
    buttons_frame,
    text="Copy",
    command=copy_password,
    font=("Segoe UI", 10, "bold"),
    bg="#374151",
    fg="white",
    activebackground="#4B5563",
    activeforeground="white",
    relief="flat",
    padx=30,
    pady=8
)

copy_button.grid(
    row=0,
    column=0,
    padx=5
)


save_button = tk.Button(
    buttons_frame,
    text="💾 Save",
    command=save_password,
    font=("Segoe UI", 10, "bold"),
    bg="#19B263",
    fg="white",
    activebackground="#1D60BF",
    activeforeground="green",
    relief="flat",
    padx=30,
    pady=8
)

save_button.grid(
    row=0,
    column=1,
    padx=5
)


# Update strength when typing manually
password_var.trace_add(
    "write",
    update_strength
)


# Generate first password
generate_password()


root.mainloop()
