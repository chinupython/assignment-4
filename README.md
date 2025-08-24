#Task 1 – Reading from a File with Exception Handling

File: Task1.py

Description:

Attempts to open and read the contents of a file named sample.txt.

If the file does not exist, it gracefully handles the error using a try-except block and displays a message.

Key Concepts Covered:

Opening and reading files in Python.

Handling FileNotFoundError exceptions.

Properly closing files after use.

Example Output:

File 'sample.txt' not found


#Task 2 – Writing, Appending, and Reading from a File

File: Task2.py

Description:

Takes user input and writes it to a file named output.txt.

Appends additional user input to the same file.

Reads and displays the final contents of the file.

Key Concepts Covered:

Writing data to a file ("w" mode).

Appending data to an existing file ("a" mode).

Reading and displaying file contents ("r" mode).

User interaction with input().

Example Run:

Enter text to write to the file : Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully written to output.txt.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
