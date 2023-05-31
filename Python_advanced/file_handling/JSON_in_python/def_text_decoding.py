import json


def text_decoding(file1: str, file2: str):
    """The program will decode the text in the text file.
    The decoding key is located in the json file."""
    with open(file1, encoding='utf-8') as json_file, open(
            file2, encoding='utf-8') as txt_file:

        data = json.load(json_file)

        txt_file = [line.strip() for line in txt_file.readlines()]

    new_text = ''

    for i in txt_file:
        for j in i:
            if j.isalpha():
                for key, value in data.items():
                    if j.upper() == key:
                        if j.isupper():
                            new_text += value
                        else:
                            new_text += value.lower()
            else:
                new_text += j
        new_text += '\n'

    print(new_text)


text_decoding(input(), input())
