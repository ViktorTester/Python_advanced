"""The program creates an alphabet dictionary, where the keys are lowercase
English characters, and the values are the ordinal numbers of
letters in the alphabet, starting from 1. Then the dictionary is serialized
and the resulting json string is stored in the json_data variable"""

from string import ascii_lowercase
import json
from pprint import pprint

alphabet = {}

for i, j in enumerate(ascii_lowercase, start=1):
    alphabet[j] = i

json_data = json.dumps(alphabet)
pprint(json_data)
