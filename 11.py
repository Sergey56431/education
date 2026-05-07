# name = input('Как вас зовут?')
# print(f'Привет, ' + name)

# Условия

# age = int(input('Введите возраст: '))
# condition = age >= 18
# if condition:
#     print('Доступ разрешён')
# else:
#     print('Доступ запрешён')
# print('программа с условием выполнилась')
#
# age = int(input('Введите возраст: '))
#
# if age < 10:
#     print('Ты ещё слишком мал')
# elif age > 70: #Это вместо else if
#     print('Вам пора спать')
# else:
#     print('Доступ запрешён')
# print('программа с условием выполнилась')

# Циклы
# По счётчику
# for i in range(1,6): # range - это диапазон от 1 до 6, выведется 1 ... 5
#     print(i)
#
# # НУЖНО СЛЕДИТЬ ЗА ОТСТУПАМИ
#
# # по условию
# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# flag = False
# while not flag:
#     pwd = input('Введите пароль: ')
#     if pwd == '123':
#         flag = True
#         print('Цикл окончен')

#
# fruits = ['Апельсин', 'Ананас', 'Яблоко']
# for fruit in fruits:
#     print(fruit)

# Задачи
# 1

# a = "Привет 'sss'"
# b = 10
# c = -2.5
# print(a)
# print(b)
# print(c)

# 2

# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
#
# print(f'Привет, {name}! Тебе - {age} лет')

# 3

# numbers = [1, 3, 5, 7, 9]
# print(f'Первый {numbers[0]}')
# print(f'Последний - {numbers[4]}')
# print(f'Последний - {numbers[-1]}')

# 4

# fruits = ('Слива','Апельсин','Груша','Банан')  # Картеж - нельзя изменять
# print(fruits[1])

# 5

# cities = {'Имя': 'Сергей', 'Возраст': 30, 'Город': 'Новосибирск'} # Это список - формат ключ: значение
# print(cities['Имя'])

# 6

# numbers = [1,2,2,3,3,4]
# print('Список', numbers)
# s_numbers = set(numbers) # Это множество и  это Коллекция с уникальными занчениями
# print('Множество', s_numbers)

# 7
#
# count = float(input('Введите число: '))
# if count > 0:
#     print('Положительное')
# elif count < 0:
#     print('Отрицательное')
# else:
#     print('Равно нулю')

# 8
# try:
#     a = int(input('Введите вашу оценку: '))
#     if a == 5:
#         print('Отлично')
#     elif a == 4:
#         print('Хорошо')
#     elif a == 3:
#         print('Удовлетворительно')
#     elif a == 2 or a == 1:
#         print('Плохо')
#     else:
#         print('Введена не корректная оценка')
# except Exception as e:
#     print(e)
#     print('Программа выполнилась но оценка не валидна')

# 9

# numbers = [1,2,3,4,5]
# for number in numbers:
#     print(number)

# 10

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# 11
#
#
# while True:
#     password = input('Введите пароль: ')
#     if password == '123':
#         print('Доступ разрешён')
#         break
#     else:
#         print('Доступ запрещён')

# # 12
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     if number == 5:
#         continue
#     print(number)

# 13

# numbers = [1,2,3,4,5]
# counts = [1,2,3]
#
# for number in numbers:
#     for count in counts:
#         print(f'{number} * {count} = {number*count}')

# 14
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# print(f'первое число - ({a}), второе число - ({b})')

# 15

# numbers = [20, 22, 29, 6, 3,1, 51]
#
# for number in numbers:
#     if  number % 2 == 0:
#         print(number)
#     if number > 50:
#         break

