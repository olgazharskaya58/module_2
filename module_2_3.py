my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список

count = 0  # начало счета
print('Список', my_list)
print('Положительные числа из списка:')

while count < len(my_list):
    num = my_list[count]  #  число из списка по порядку
    count = count + 1  # каждое следующее число
    if num == 0:
        continue  #  0 - не отрицательное и не положительное число.
    elif num < 0:
        print('Встретилось отрицательное число:', num)
        break
    elif count == len(my_list):
        print(num)
        print('Список закончился')
    else:
        print(num)
