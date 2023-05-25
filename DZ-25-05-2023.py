####   "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
glasnyye = 'уеиаоєяію'
my_string = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'
my_words = my_string.split() ##Преобразуем предложение в список слов

print(my_words)

i=0  ##Счётчик
for word in my_words:  ##Перебор всех слов в списке
    for letter in word: ##Перебор каждой буквы в слове
        if letter in glasnyye: ###Проверка на согласную
            my_words[i] = my_words[i].replace(letter, '#') ##Замена букв и переопределение слова в списке
    i += 1 
print(my_words)

new_line = ''
for word in my_words: ##Перебор всех слов в списке
    new_line = new_line + word + ' ' ### Добавляем каждое слово к пустой строке в циклеі

print (new_line) 

