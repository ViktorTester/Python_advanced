"""The function takes a filename and finds the longest word within its contents
and returns it as a response. If there are multiple words with a maximum length,
the word that occurs last in the text is returned."""

from string import punctuation


def longest_word_in_file(file_name: str) -> str:
    with open(file_name, encoding='utf-8') as file:
        longest_word = ''
        for i in file.read().split():
            i = i.strip(punctuation)
            if len(i) >= len(longest_word):
                longest_word = i

    return longest_word


print(longest_word_in_file(input()))