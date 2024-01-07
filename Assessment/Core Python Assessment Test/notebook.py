"""Write a program to demonstrate the Python E-Note Book Console based
application"""

import datetime

def generate_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = f"{timestamp}\nTitle: {title}\nContent: {content}\n\n"
    
    with open("notes.txt", "a") as file:
        file.write(note)
    
    print("Note added successfully!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            print("------ All Notes ------")
            print(notes)
            print("------------------------")
    except FileNotFoundError:
        print("No notes found.")


import notebook

def display_menu():
    print("\n----- Menu -----")
    print("1. Generate Note")
    print("2. View Notes")
    print("3. Exit")
    print("-----------------")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            notebook.generate_note()
        elif choice == "2":
            notebook.view_notes()
        elif choice == "3":
            print("Exiting the E-Note Book. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option.")

main()