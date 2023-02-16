def generate_letter(mail, name, date, time, place, teacher='Ilon Musk', number=17):
    return f'To: {mail} \n' \
           f'Hello, {name}! \n' \
           f'You have an exam that will take place o {date}, at {time}. \n' \
           f'At: {place}. \n' \
           f'The exam will be conducted by the {teacher} in the classroom {number}. \n' \
           f'We wish you good luck on the exam!'


print(generate_letter('lara@yandex.ru', 'Jack', '10th of december', '12:00', 'Groove street, number 2'))
print()
print(generate_letter('lara@yandex.ru', 'Jack', '10th of december', '12:00',
                      'Groove street, number 2', 'Tereza May', 23))

# The generate_letter() function generates an email according to a template:

# To: <mail>
# Hello <name>!
# You have an exam that will take place on <date>, at <time>.
# At: <place>.
# The exam will be conducted by the <teacher> in the classroom <number>.
# We wish you good luck on the exam!

# The function receives five required arguments mail, name, date, time, place and two
# optional teacher, number as input and returns the text of the finished letter.
# If there is no teacher argument, the teacher will be Ilon Musk,
# and if there is no number argument, then the classroom will be 17.
