###List (Список):
my_list = [] #пустой список
my_list.append(1)
my_list.append(30)
my_list.append(25)   #добавляем числа (жаль что нельзя одним разом добавить сразу 3 значения)
print(my_list) #выводим список
index = my_list.index(30)
print(index)## так можно узнать индекс значения
my_list[1] = 8 ### меняем значение
print(my_list)
my_list.remove(25) ##удалить значение из списка
print(my_list)


my_list_2 = [10, 21, 40, 50,70,90]
my_list.extend(my_list_2) ### эта функа для добавления значений из второго списка в конец первого
print(my_list)
sliced_list = my_list [2:5] ## функа для среза
print(sliced_list) ###  выводим срез чисел

##String (Рядок):

name = 'oleksandra'
print (name.capitalize()) ## функа делает первую букву заглавной
#count_letters =len(name) не обязательно (функа len и так выведет кол-во букв)
print (len(name)) #вывод кол-во букв

### Tuple

list = [12,20,22,'sasha',15]
my_tuple = tuple(list)
print(my_tuple)         ## можно просто сразу создать тапл list_sasha = (1, 1, 2, 2, 4)
#my_tuple[1] = 'ruslan'      ## убеждаемся что значения в тапле не подлежат редактированию
print(my_tuple)


list_sasha = (1, 1, 2, 2, 4)
print(type(list_sasha)) # проверка типа списка
merged_tuple = my_tuple + list_sasha ##функа для обьединения таплов
print(merged_tuple)


#Set (Множина):
set_1 = {1, 2, 3, 4}
print(type(set_1))
print(set_1)
set_1.add(5)  #добавить значение
print(set_1)
set_1.remove(3) # убрать значение
print(set_1)

# Frozenset (Незмінювана множина):
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)
my_frozenset.add(4) # фрозенсет нельзя редактировать / убеждаемся что будет ошибка
Sasha_din = frozenset([1,78,25,5])
print(type(Sasha_din))
merged_frozenset = my_frozenset | Sasha_din # функа которая обьединяет фрозенсет
print(merged_frozenset)

#Dict (Словник):
Food = {
    "pizza": "italia",
    "borsh": "Ukraine",
    "Sushi": "japen"
} #создаем справочник
print(Food)
Food["tom-yam"] = "Thailand" #просто присваиваем новое значение и оно добавится
print(Food)
del Food ["borsh"] #функа для удаления
print(Food)








