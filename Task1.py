
try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File 'sample.txt' not found")
