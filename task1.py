# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью  символьной графики.
# Для вертикальных линий используйте символ вертикального штриха (|), а для горизонтальных — дефис (-).
# Пусть ширину и высоту рамки определяет пользователь.

width = int(input('Enter the width of the frame:'))
height = int(input('Enter the height of the frame: '))
for row in range(height + 1):
    for col in range(width + 1):
        if col == width or col == 0:
            print(' | ', end = '')
        elif row == height or row == 0:
            print(' - ', end = '')
        else:
            print(' ', end = '')

print()
