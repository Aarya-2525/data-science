with open("my_log.txt", "w") as file:
    file.write("Hello World! I'm writing on this file\n")
    file.write("This is Day 1 of learning Python!\n")

with open("my_log.txt", "r") as file:
    print("File Contents (Read Mode):\n")
    print(file.read())

with open("my_log.txt", "a") as file:
    file.write("This line was appended.")

with open("my_log.txt", "r") as file:
    print("After Appending:\n")
    print(file.read())