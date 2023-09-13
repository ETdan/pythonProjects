from tkinter import *
from tkinter import messagebox
import random
import pyclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "" .join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_file():
    username = username_input.get()
    password = password_input.get()
    website = website_input.get()

    new_data = {
        website: {
            "Email:": username,
            "Password:": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="warning", message="you missed a box")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search_file():
    search_input = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="Data file not found")
    finally:
        if search_input in data:
            password = data[search_input]["Password"]
            email = data[search_input]["Email"]
            messagebox.showinfo(title=f"{search_input}", message=f"Email: {email}\nPassword: {password}")
            print(password, email)
        else:
            messagebox.showinfo(title=f"{search_input}", message="No such data")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image_url = PhotoImage(file="logo.png")
image_holder = Canvas(height=200, width=200)
image_holder.create_image(100, 100, image=image_url)
image_holder.grid(column=1, row=0)

# Label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username")
username_label.grid(column=0, row=2)

Password_label = Label(text="Password")
Password_label.grid(column=0, row=3)

# Entry
website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1)

username_input = Entry(width=35)
username_input.insert(0, "example@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="add", width=36, command=add_to_file)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=21, command=search_file)
search_button.grid(column=2, row=1)


window.mainloop()
