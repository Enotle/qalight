#test_str = '12'
#test_var = 'Length my str: ' + str(len(test_str))
#print('My test string: ' + test_str)
#print('Length my str: ' + str(len(test_str)))


####
###         0    1    2    3   ###########
my_list = ['a', 'b', 'c', 'd']
#####        012               ###########
my_string = 'asd'

count = 0
for i in my_list:
    print('Current symbol: ' + i)
    print(my_list[count])
    count += 1


####   "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
glasnyye = 'уеиаоєяію'
my_string = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'
my_words = my_string.split()
print(my_words)

for word in my_words:
    for i in word:
        if i in glasnyye:
            word.replace(i, '#')
print(my_words)
