import tkinter as tk
import pyttsx3
import datetime
import time

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Create a list to store the daily tasks
tasks = []

# Set the interval for the reminder (in seconds)
interval = 3600

# Create a function to remind the user of their tasks
def remind():
    # Get the current time
    now = datetime.datetime.now()

    # Check if it is morning, afternoon, or evening
    if now.hour < 12:
        greeting = "Good morning! Here are your tasks for the day:"
    elif now.hour < 18:
        greeting = "Good afternoon! Here are your tasks for the day:"
    else:
        greeting = "Good evening! Here are your tasks for the day:"

    # Speak the greeting and list of tasks
    engine.say(greeting)
    for task in tasks:
        engine.say(task)
    engine.runAndWait()

# Create a function to run the reminder at regular intervals
def run_reminder():
    while True:
        remind()
        time.sleep(interval)

# Create the main window
window = tk.Tk()
window.title("Daily Task Reminder")

# Create a function to add a new task to the list
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)

# Create a function to clear all tasks from the list
def clear_tasks():
    tasks.clear()
    task_list.delete(0, tk.END)

# Create a label and entry field for adding new tasks
task_label = tk.Label(window, text="Enter a new task:")
task_entry = tk.Entry(window)

# Create a button for adding tasks
add_button = tk.Button(window, text="Add Task", command=add_task)

# Create a listbox for displaying the tasks
task_list = tk.Listbox(window)

# Create a button for clearing all tasks
clear_button = tk.Button(window, text="Clear Tasks", command=clear_tasks)

# Create a button for starting the reminder loop
start_button = tk.Button(window, text="Start Reminder", command=run_reminder)

# Pack the widgets into the window
task_label.pack()
task_entry.pack()
add_button.pack()
task_list.pack()
clear_button.pack()
start_button.pack()

# Run the main loop
window.mainloop()
