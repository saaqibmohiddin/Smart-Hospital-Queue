import tkinter as tk
from tkinter import messagebox

queue = []

def add_patient():
    name = entry_name.get()

    if name == "":
        messagebox.showwarning("Warning", "Enter patient name")
        return

    queue.append(name)

    token = len(queue)
    waiting_time = token * 10

    messagebox.showinfo(
        "Patient Added",
        f"Token Number: {token}\nWaiting Time: {waiting_time} minutes"
    )

    entry_name.delete(0, tk.END)
    update_queue()

def call_next():
    if len(queue) == 0:
        messagebox.showinfo("Info", "No patients waiting")
        return

    patient = queue.pop(0)

    messagebox.showinfo(
        "Now Serving",
        patient
    )

    update_queue()

def update_queue():

    queue_box.delete(0, tk.END)

    for i, patient in enumerate(queue, start=1):
        queue_box.insert(tk.END, f"{i}. {patient}")

root = tk.Tk()

root.title("Smart Hospital Queue System")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Smart Hospital Queue System",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=10)

btn_add = tk.Button(
    root,
    text="Add Patient",
    command=add_patient
)
btn_add.pack(pady=5)

btn_call = tk.Button(
    root,
    text="Call Next Patient",
    command=call_next
)
btn_call.pack(pady=5)

queue_box = tk.Listbox(root, width=40, height=10)
queue_box.pack(pady=10)

root.mainloop()