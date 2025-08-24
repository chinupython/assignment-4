text = input("Enter text to write to the file : ")
file = open("output.txt", "w")
file.write(text + "\n")
print("Data successfully written to output.txt.\n")

extra_text = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(extra_text + "\n")
print("Data successfully written to output.txt.\n")

file = open("output.txt", "r")
content = file.read()
print("Final content of output.txt:")
print(content)