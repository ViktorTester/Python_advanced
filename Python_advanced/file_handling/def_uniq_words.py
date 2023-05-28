"""The program receives a test document as input and counts how many unique words
it contains. The answer is displayed as a dictionary, where the key is a
unique word and the value is the number of times it occurs in the text."""
def uniq_words():
    with open('C:/Users/vikto/Desktop/lorem.txt', encoding='utf-8') as file:
        words = {}
        for i in file.read().lower().split():
            words[i.upper()] = words.get(i.upper(), 0) + 1

    return words