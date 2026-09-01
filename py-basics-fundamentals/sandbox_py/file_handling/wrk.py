# 1. Challenge 4: Missing File Handling
filename = input("Enter filename to open: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print(data) 
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

# 2. Challenge 1: Creating & Writing
lines_to_write = [
    "Day 1: Started learning Python file handling.\n",
    "Day 2: Practice makes progress.\n",
    "Day 3: Building muscle memory.\n"
]

with open("journal.txt", "w") as file:
    file.writelines(lines_to_write)

# 3. Challenge 3: Appending Data
with open("journal.txt", "a") as file:
    file.write("Day 4: Mastered append mode!\n")

# 4. Challenge 2: Reading Line-by-Line efficiently
with open("journal.txt", "r") as file:
    for count, line in enumerate(file, start=1):
        print(f"{count}: {line.strip()}")