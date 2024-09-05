# Задача 5. Игра «Компьютер угадывает число»
# Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
# спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
# трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов
# мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.


number1, number2 = 1, 100
while True:
    N = (number1 + number2) // 2
    print("Твоё число равно, меньше или больше, чем число", N, "?")
    n = int(input("1 - равно, 2 - больше, 3 - меньше: "))
    if n == 3:
        print("Я угодал!")
        break
    elif n == 1:
        number1 = n
    else:
        number2 = n
