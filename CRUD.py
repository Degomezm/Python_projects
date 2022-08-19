#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox, Tk
import sqlite3


# Add Functions for the app
# Connect to the database
def db_connection():
    connection = sqlite3.connect("Users")
    cursor_connection = connection.cursor()
    try:
        cursor_connection.execute("""
            CREATE TABLE USERDATA (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME_USER VARCHAR(50),
            PASSWORD VARCHAR(50),
            LASTNAME VARCHAR(50),
            ADDRESS VARCHAR(50),
            COMMENT VARCHAR(100))
            """)
        messagebox.showinfo("BBDD", "BBDD was create successfully")
    except:
        messagebox.showwarning("¡Attention!", "BBDD already exists")


# Exit to the database
def exit_application():
    exit_option = messagebox.askquestion("Close", "¿Do you want to exit the application?")
    if exit_option == "yes":
        root.destroy()


# Clean all the fields from the interface
def clean_fields():
    user_id.set("")
    user_name.set("")
    user_password.set("")
    user_lastname.set("")
    user_address.set("")
    field_comment.delete(1.0, END)


# Create a record for a user
def create():
    connection = sqlite3.connect("Users")
    cursor_connection = connection.cursor()
    cursor_connection.execute("INSERT INTO USERDATA VALUES(NULL,?, ?, ?, ?, ?)", (user_name.get(), user_password.get(),
                                                                                  user_lastname.get(),
                                                                                  user_address.get(),
                                                                                  field_comment.get("1.0", END)))

    connection.commit()
    messagebox.showinfo("BBDD", "Record inserted successfully")


# Retrieve the information from a user
def read():
    connection = sqlite3.connect("Users")
    cursor_connection = connection.cursor()
    cursor_connection.execute("SELECT * FROM USERDATA WHERE ID=?", user_id.get())
    user = cursor_connection.fetchall()

    for field in user:
        user_id.set(field[0])
        user_name.set(field[1])
        user_password.set(field[2])
        user_lastname.set(field[3])
        user_address.set(field[4])
        field_comment.insert(1.0, field[5])

    connection.commit()


# Update the information from a user
def update():
    connection = sqlite3.connect("Users")
    cursor_connection = connection.cursor()
    cursor_connection.execute(
        "UPDATE USERDATA SET NAME_USER=?, PASSWORD=?, LASTNAME=?, ADDRESS=?, COMMENT=? WHERE ID=?",
        (user_name.get(), user_password.get(), user_lastname.get(), user_address.get(),
         field_comment.get("1.0", END), user_id.get()))

    connection.commit()
    messagebox.showinfo("BBDD", "Record updated successfully")


# Delete an user record
def delete():
    connection = sqlite3.connect("Users")
    cursor_connection = connection.cursor()
    cursor_connection.execute("DELETE FROM USERDATA WHERE ID=?", user_id.get())
    connection.commit()
    messagebox.showinfo("BBDD", "Record deleted successfully")


# Graphic interface
root: Tk = Tk()

# Create the main menubar
menubar = Menu(root)
root.config(menu=menubar, width=300, height=300)

# create database Menubar
bbddmenu = Menu(menubar, tearoff=0)
bbddmenu.add_command(label="Connect", command=db_connection)
bbddmenu.add_command(label="Disconnect", command=exit_application)

# Erase Menubar
cleanmenu = Menu(menubar, tearoff=0)
cleanmenu.add_command(label="Clean Fields", command=clean_fields)

# CRUD Menubar
crudmenu = Menu(menubar, tearoff=0)
crudmenu.add_command(label="Create", command=create)
crudmenu.add_command(label="Read", command=read)
crudmenu.add_command(label="Update", command=update)
crudmenu.add_command(label="Delete", command=delete)

# Help Menubar
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Licence")
helpmenu.add_command(label="About...")

# Add the options to the menubar
menubar.add_cascade(label="BBDD", menu=bbddmenu)
menubar.add_cascade(label="Clean", menu=cleanmenu)
menubar.add_cascade(label="CRUD", menu=crudmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

# Create Frame and fields of data collection
first_frame = Frame(root)
first_frame.pack()
user_id = StringVar()
user_name = StringVar()
user_lastname = StringVar()
user_password = StringVar()
user_address = StringVar()

# Add fields of information entry
field_id = Entry(first_frame, textvariable=user_id)
field_id.grid(row=0, column=1, padx=10, pady=10)
field_name = Entry(first_frame, textvariable=user_name)
field_name.grid(row=1, column=1, padx=10, pady=10)
field_name.config(fg="blue")
field_password = Entry(first_frame, textvariable=user_password)
field_password.grid(row=2, column=1, padx=10, pady=10)
field_password.config(show="*")
field_lastname = Entry(first_frame, textvariable=user_lastname)
field_lastname.grid(row=3, column=1, padx=10, pady=10)
field_address = Entry(first_frame, textvariable=user_address)
field_address.grid(row=4, column=1, padx=10, pady=10)
field_comment = Text(first_frame, width=20, height=5)
field_comment.grid(row=5, column=1, padx=10, pady=10)
scroll_comment = Scrollbar(first_frame, command=field_comment.yview)
scroll_comment.grid(row=5, column=2, sticky="nsew")
field_comment.config(yscrollcommand=scroll_comment.set)

# Add field Labels
id_label = Label(first_frame, text="Id:")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
name_label = Label(first_frame, text="Name:")
name_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
password_label = Label(first_frame, text="Password:")
password_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
lastname_label = Label(first_frame, text="LastName:")
lastname_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)
address_label = Label(first_frame, text="Address:")
address_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)
comment_label = Label(first_frame, text="Comment:")
comment_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# Create Frame
second_frame = Frame(root)
second_frame.pack()

# Add Buttons
create_button = Button(second_frame, text="Create", command=create)
create_button.grid(row=0, column=0, sticky="e", padx=10, pady=10)
read_button = Button(second_frame, text="Read", command=read)
read_button.grid(row=0, column=1, sticky="e", padx=10, pady=10)
update_button = Button(second_frame, text="Update", command=update)
update_button.grid(row=0, column=2, sticky="e", padx=10, pady=10)
delete_button = Button(second_frame, text="Delete", command=delete)
delete_button.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
