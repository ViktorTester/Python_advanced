from gtts import gTTS
from playsound import playsound

text_val = "Elizabeth II was Queen of the United Kingdom and other Commonwealth realms from 6 February 1952 until her " \
           "death in 2022. She was queen regnant of 32 sovereign states during her lifetime, and was head of state of " \
           "15 realms at the time of her death. Her reign of 70 years and 214 days was the longest of any British " \
           "monarch and the longest verified reign of any female monarch in history. "

language = 'en'

obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("test.mp3")

playsound("test.mp3")