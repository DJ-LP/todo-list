import tkinter as tk

from tkinter import messagebox

import os



tasks = []  

file_name = "tasks.txt"  



def load_tasks():


    if os.path.exists(file_name):

        with open(file_name, "r") as file:

            for line in file:

                task_data = line.strip().split(" | ")

                tasks.append({"task": task_data[0], "deadline": task_data[1], "priority": task_data[2]})

        update_task_list()



def save_tasks():

    """Safe dates as an .txt file"""

    with open(file_name, "w") as file:

        for task in tasks:

            file.write(f"{task['task']} | {task['deadline']} | {task['priority']}\n")



def add_task():



    task = task_entry.get()

    deadline = deadline_entry.get()

    priority = priority_var.get()

    

    if task and deadline and priority:

        tasks.append({"task": task, "deadline": deadline, "priority": priority})

        update_task_list()

        task_entry.delete(0, tk.END)

        deadline_entry.delete(0, tk.END)

        save_tasks()

    else:

        messagebox.showwarning("ERROR", "Pleas fill all Boxes!")



def remove_task():

    """Entfernt die ausgewählte Aufgabe."""

    selected = task_list.curselection()

    if selected:

        tasks.pop(selected[0])

        update_task_list()

        save_tasks()

    else:

        messagebox.showwarning("ERROR", "Pleas select an task!")



def sort_tasks():

    priority_map = {"High": 1, "Medium": 2, "Low": 3}

    tasks.sort(key=lambda x: priority_map.get(x["priority"], 3))

    update_task_list()

    save_tasks()



def update_task_list():


    task_list.delete(0, tk.END)  

    for task in tasks:
        task_text = f"{task['task']} (until: {task['deadline']}, Priority: {task['priority']})"
        task_list.insert(tk.END, task_text)

        index = task_list.size() - 1
        if task["priority"] == "High":
            task_list.itemconfig(index, {'bg': 'red', 'fg': 'white'})
        elif task["priority"] == "Medium":
            task_list.itemconfig(index, {'bg': 'yellow', 'fg': 'black'})
        elif task["priority"] == "Low":
            task_list.itemconfig(index, {'bg': 'green', 'fg': 'white'})


root = tk.Tk()

root.title("To-Do-Liste")




task_label = tk.Label(root, text="Tasks:")

task_label.grid(row=0, column=0, padx=10, pady=5)

task_entry = tk.Entry(root, width=30)

task_entry.grid(row=0, column=1, padx=10, pady=5)



deadline_label = tk.Label(root, text="Deadline:")

deadline_label.grid(row=1, column=0, padx=10, pady=5)

deadline_entry = tk.Entry(root, width=30)

deadline_entry.grid(row=1, column=1, padx=10, pady=5)



priority_label = tk.Label(root, text="Priority:")

priority_label.grid(row=2, column=0, padx=10, pady=5)

priority_var = tk.StringVar(value="Medium")

priority_dropdown = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")

priority_dropdown.grid(row=2, column=1, padx=10, pady=5)





add_button = tk.Button(root, text="Add task", command=add_task)

add_button.grid(row=3, column=0, columnspan=2, pady=10)



remove_button = tk.Button(root, text="Delet task", command=remove_task)

remove_button.grid(row=4, column=0, columnspan=2, pady=10)



sort_button = tk.Button(root, text="Sort tasks", command=sort_tasks)

sort_button.grid(row=5, column=0, columnspan=2, pady=10)



task_list = tk.Listbox(root, width=60, height=15, activestyle='none')

task_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)





load_tasks()




root.mainloop()


