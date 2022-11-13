letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
         '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']

text = input().upper()
new_dict = dict(zip(letters, morse))

for i in range(len(text)):
    for key, value in new_dict.items():
        if text[i] in key:
            print(value, end=' ')

# The program encodes a text message according to Morse code.