

phone = input ("Phone: ")

digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "eight": "eight",
    "nine": "nine"
}

output = ""


for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)