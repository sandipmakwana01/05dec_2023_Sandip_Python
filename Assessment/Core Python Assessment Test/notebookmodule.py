import os

def generate_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    try:
        with open(f"{title}.txt", "w") as file:
            file.write(content)
        print("Note successfully generated!")
    except Exception as e:
        print(f"Error: {e}. Please try again.")

def view_notes():
    try:
        print("\n*** List of Notes ***")
        files = [f for f in os.listdir('.') if f.endswith(".txt")]
        if not files:
            print("No notes found.")
        else:
            for file in files:
                with open(file, "r") as note_file:
                    content = note_file.read()
                    print(f"\nTitle: {file.replace('.txt', '')}\nContent: {content}")
    except Exception as e:
        print(f"Error: {e}. Please try again.")
