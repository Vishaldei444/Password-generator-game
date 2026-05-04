# Password Manager using Tkinter

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import random
import string
import pyperclip
from PIL import Image, ImageTk
from datetime import datetime

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password():
    characters = string.ascii_letters + string.digits + "@#$%&*"
    password = ''.join(random.choice(characters) for _ in range(14))

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------- COPY PASSWORD ---------------- #

def copy_password():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- SAVE PASSWORD ---------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Empty field check
    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    # Gmail validation
    if "@" not in email or not email.endswith("@gmail.com") or email.startswith("@"):
        messagebox.showerror("Error", "Enter valid Gmail address ❌")
        return

    # Save data
    with open("password_data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

    messagebox.showinfo("Success", "Password Saved Successfully ✅")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------- SEARCH PASSWORD ---------------- #

def search_password():
    website = website_entry.get()

    try:
        with open("password_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(" | ")

                if data[0] == website:
                    email_entry.delete(0, END)
                    email_entry.insert(0, data[1])

                    password_entry.delete(0, END)
                    password_entry.insert(0, data[2])

                    messagebox.showinfo("Found", "Password Found")
                    return

        messagebox.showerror("Not Found", "No Data Found")

    except FileNotFoundError:
        messagebox.showerror("Error", "No database file found")

# ---------------- SHOW / HIDE PASSWORD ---------------- #

def show_hide_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_btn.configure(text="Hide")
    else:
        password_entry.config(show="*")
        show_btn.configure(text="Show")

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Password Generator by Vishal")
root.geometry("1000x600")
root.resizable(False, False)

# ---------------- BACKGROUND IMAGE ---------------- #

bg_image = Image.open("lock.jpg")
bg_image = bg_image.resize((1000, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

# ---------------- DATE & TIME ---------------- #

date_now = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%I:%M %p")

Label(root, text=date_now,
      font=("Arial", 18, "bold"),
      bg="#002244",
      fg="white").place(x=20, y=20)

Label(root, text=time_now,
      font=("Arial", 18, "bold"),
      bg="#002244",
      fg="white").place(x=800, y=20)

# ---------------- HEADING ---------------- #

Label(root,
      text="Built to be secure...",
      font=("Arial", 28, "bold"),
      bg="#003366",
      fg="white").place(x=350, y=100)

# ---------------- LABELS ---------------- #

Label(root, text="Website URL:",
      font=("Arial", 18, "bold"),
      bg="#003366",
      fg="white").place(x=430, y=220)

Label(root, text="Email/Username:",
      font=("Arial", 18, "bold"),
      bg="#003366",
      fg="white").place(x=390, y=290)

Label(root, text="Password:",
      font=("Arial", 18, "bold"),
      bg="#003366",
      fg="white").place(x=470, y=360)

# ---------------- ENTRIES ---------------- #

website_entry = Entry(root, width=30, font=("Arial", 9))
website_entry.place(x=650, y=225)

email_entry = Entry(root, width=30, font=("Arial", 12))
email_entry.place(x=650, y=295)

password_entry = Entry(root, width=30, font=("Arial", 9), show="*")
password_entry.place(x=650, y=365)

# ---------------- BUTTONS ---------------- #

search_btn = Button(root,
                    text="Search",
                    font=("Arial", 10, "bold"),
                    bg="#003f7f",
                    fg="white",
                    width=10,
                    command=search_password)
search_btn.place(x=900, y=220)

generate_btn = Button(root,
                      text="Generate",
                      font=("Arial", 10, "bold"),
                      bg="#003f7f",
                      fg="white",
                      command=generate_password)
generate_btn.place(x=900, y=360)

show_btn = ctk.CTkButton(
    master=root,
    text="Show",
    font=("Arial", 10, "bold"),
    fg_color="#003f7f",
    text_color="white",
    hover_color="#002855",
    command=show_hide_password
)
show_btn.place(x=650, y=410)

copy_btn = ctk.CTkButton(
    master=root,
    text="Copy",
    font=("Arial", 10, "bold"),
    fg_color="#003f7f",
    text_color="white",
    hover_color="#002855",
    command=copy_password
)
copy_btn.place(x=860, y=410)

add_btn = Button(root,
                 text="ADD",
                 font=("Arial", 12, "bold"),
                 bg="#004c99",
                 fg="white",
                 width=35,
                 command=save_password)
add_btn.place(x=450, y=500)

# ---------------- MAIN LOOP ---------------- #

root.mainloop()