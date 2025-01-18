#To-Do List Application

## Overview
A **Phython-based To-Do List Application** with a graphical user interface (GUI) built using **Tkinter**. This application helps you manage tasks by adding, removing and sorting them by priority. tasks are saved locally, ensuring persistence across sessions.

---

## Features
- **Add Tasks**: Enter tasks withdeadlines and a priority level (High, Medium, Low).
- **Remove Tasks**: Select a task and delete it from the list.
- **Sort Tasks**: Automatically sort tasks by their priority.
- **Peristent storage**: Tasks are saved in 'tasks.txt' and loaded when reopening the app.
- **Priority Visualization**: Task are color-coded:
    - **High Priority**: Red
    - **Medium Priority**: Yellow
    - **Low Priority**: Green

---

## Installation

### Prerequisites
- **Python 3.x**: Ensure you have Python installed. [Download Phython](https://www.python.org/downloads/)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/DJ-LP/todo-list-app.git
    cd todo-list-app
2. Run the application:
    ```bash
    python todo_list.py

## Usage 

### 1.Launch the App: Run the script to open the GUI
### 2.Add a Task:
    -Input a task description.
    -Provied a deadline (e.g., dd.mm,yyyy).
    -Select a priority level from the dropdown.
    -Cick Add Task.
### 3.Remove a Task: Select a task from the list and click Remove Task.
### 4.Sort Tasks: Click Sort tasks to arrange them by priority.

## File Structure
### todo_list.py: Main application code.
### tasks.txt: File where tasks are saved. This is created automatically upon the first run.


