"""Write a program to demonstrate the Python E-Note Book Console based
application"""

import notebookmodule

def main():
    while True:
        print("\n*** E-Note Book Console Application ***")
        print("1. Generate Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            notebookmodule.generate_note()
        elif choice == '2':
            notebookmodule.view_notes()
        elif choice == '3':
            print("Exiting the E-Note Book. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
