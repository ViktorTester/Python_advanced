emails = {
    'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
    'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
    'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
    'yandex.ru': ['surface', 'google'],
    'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
    'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']
}

arr = []

for key, value in emails.items():
    for i in range(len(value)):
        arr.append(value[i] + '@' + key)

arr.sort()

print(*arr, sep='\n')

# The 'emails' dictionary contains information about the email addresses of users
# grouped by domain. The program displays all email addresses in alphabetical order,
# each on a separate line, in the format username@domain.
