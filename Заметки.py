def say_hello(): #создание функции
    print("Hello world") #что выводить при вызове функции

say_hello() #вызов функции


def My_pro():
    user_input = input("Введіть число: ") # что программа должна сказать при вызове функции

    try:
        number = int(user_input) # тут мы указываем что значение должно быть числом
        print("Ви ввели число:", number)
    except ValueError: #перехват ошибки
        print("Entered not valid data")


#My_pro()


def new_pro(string1, string2): # создаем функцию и прописываем аргументы
    try:
        part1 = int(string1)  #указываем что должны быть числа
        part2 = int(string2)
        result = part1 + part2  #указываем что результатом должно быть сложение чисел
        print("Сума чисел:", result) #при написании двух чисел вывести результат
    except ValueError:
        result = string1 + string2  # перехватываем ошибку и склеиваем
        print("Конкатенація рядків:", result)

new_pro("10", "25")
new_pro("как", "дела")
new_pro("10", "дней")


def new_pro_2():
    while True:   #цикл работает до тех пор пока не будет введено верное значение
        user_input = input("please enter a number: ")

        try:
            number = float(user_input)  #флоат позволяет вводить и числа и дроби
            print("thanks you entered the number", number)
            break  # конец цикла если введено верное значение
        except ValueError:
            print("The value entered is not a number. Please try again.")


new_pro_2()