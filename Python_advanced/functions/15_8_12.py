data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа',
        'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна',
        'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

result = sorted(data, key=lambda x: (len(x), x))

print(*result)

# The 'data' list contains words. The program sorts it in ascending word length,
# and then in lexicographic order. The sorted words are displayed on one line,
# separated by a space character.

# If the word lengths match, sorting occurs in lexicographic order.