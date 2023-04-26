# Python-Reminder-Script

This is a simple Python program that reminds you of your daily tasks at regular intervals. It uses text-to-speech technology to speak the tasks out loud, so you don't have to keep checking your to-do list.

## Prerequisites
    Python 3.x
    Tkinter (Python's standard GUI package)
    Pyttsx3 (Python library for text-to-speech conversion)
    A compatible operating system (tested on Windows 10)

## Getting started

1. Clone this repository or download the source code.
2. Install the required packages (Tkinter and Pyttsx3) if you haven't already.
3. Run the `reminder.py` file.

## How to use

1. Enter your tasks in the text box and click the "Add Task" button to add them to the list.
2. Click the "Start Reminder" button to start the reminder loop.
3. The program will remind you of your tasks at regular intervals (default is every hour).
4. Click the "Clear Tasks" button to clear all tasks from the list.

## Customization
-> You can customize the interval between reminders by changing the interval variable (in seconds) in the code.

-> You can customize the greeting for each reminder by editing the `remind()` function in the code.

## Limitations
-> The program only runs on a compatible operating system and with the required packages installed.

-> The program uses a simple while loop to run the reminder at regular intervals, which may not be the most efficient method.

-> The program relies on the user to enter tasks manually and does not support importing tasks from external sources.

## License

This project is licensed under MIT License. Check the license file for more information.        
