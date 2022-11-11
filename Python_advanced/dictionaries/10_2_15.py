nokia = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
text = input().upper()

for i in range(len(text)):
    for key, value in nokia.items():
        if text[i] in value:
            x = list(value)
            combo = x.index(text[i])
            print(key * (combo + 1), end='')

# On mobile feature phones, you can send text messages using the numeric keypad.
# Since there are several letters associated with each key, most letters require
# multiple keystrokes. Pressing a number once generates the first character specified
# for that key. Pressing the number 2, 3, 4, or 5 times
# generates the second, third, fourth, or fifth character of the key.

# The program displays the keystrokes required for the entered message.

# The input to the program is one line - a text message.
