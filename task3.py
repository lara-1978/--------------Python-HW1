# Задача 3. Простые числа
# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу.
# Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла.
# Одна итерация — одно число.
# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.
# Количество простых чисел в последовательности: 4.


N = int(input(' Введите  длину последовательности: '))
counter = 0

for a in range(N):
    number = int(input('Введите число: '))
    for divider in range(2, number):
        if number % divider == 0:
            counter += 1
            break
print('Кол-во простых чисел:', N - counter)
