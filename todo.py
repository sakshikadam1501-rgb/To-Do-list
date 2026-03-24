import json
import os
from colorama import Fore, init

init(autoreset=True)

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    print(Fore.CYAN + "\n===== YOUR TASKS =====")
    if not tasks:
        print(Fore.RED + "No tasks available")
        return

    for i, t in enumerate(tasks, 1):
        status = Fore.GREEN + "DONE" if t["done"] else Fore.YELLOW + "PENDING"
        print(f"{i}. {t['title']} → {status}")

tasks = load_tasks()

while True:
    print(Fore.MAGENTA + "\n====== TO DO MENU ======")
    print("1 Add Task")
    print("2 View Task")
    print("3 Complete Task")
    print("4 Delete Task")
    print("5 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(Fore.GREEN + "Task Added")

    elif ch == "2":
        show_tasks(tasks)

    elif ch == "3":
        show_tasks(tasks)
        n = int(input("Task number: "))
        tasks[n-1]["done"] = True
        save_tasks(tasks)
        print(Fore.GREEN + "Task Completed")

    elif ch == "4":
        show_tasks(tasks)
        n = int(input("Task number: "))
        tasks.pop(n-1)
        save_tasks(tasks)
        print(Fore.RED + "Task Deleted")

    elif ch == "5":
        print(Fore.CYAN + "Goodbye 👋")
        break