# Chistian Dating | BSCPE 1-5

# Write a method in python to write multiple line of text contents into a text file mylife.txt

input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" * 80)

# Intro
import pyfiglet
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "Thin"))

# Pseudocode
# open mylife.txt (write)
with open("mylife.txt", "w") as f:
# input
    while True:
        word = input("Enter line: ")
        f.write(word + "\n")
# yes (y), or no (n)
        while True:
            choice = input("Are there more lines y/n? ")
# if y
            if choice.lower() == "y":
                break
            elif choice.lower() != "y" and choice.lower() != "n":
                print("Answer must be y or n only.")
            else:
                break
# if n
# START
