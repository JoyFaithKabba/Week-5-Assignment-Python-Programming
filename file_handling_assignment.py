# file_handling_assignment.py

# File Creation
def create_file():
    try:
        # Open a new file in write mode
        with open("my_file.txt", "w") as file:
            # Write some lines with strings and numbers
            file.write("This is the first line.\n")
            file.write("This is line number 2.\n")
            file.write("The number is 12345.\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

# File Reading and Display
def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nFile content after reading:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File Appending
def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1.\n")
            file.write("Appended line 2.\n")
            file.write("Appended line 3.\n")
        print("Content appended to the file.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Main function to demonstrate the file handling tasks
def main():
    try:
        # Step 1: Create file and write initial content
        create_file()

        # Step 2: Read and display file content
        read_file()

        # Step 3: Append new lines to the file
        append_to_file()

        # Step 4: Read and display file content again after appending
        read_file()

    except PermissionError:
        print("Error: You do not have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling tasks completed.")

# Run the main function
if __name__ == "__main__":
    main()
