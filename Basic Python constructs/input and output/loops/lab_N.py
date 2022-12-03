"""
Один из самых интересных видов чисел в математике — простые числа. Их объединяет то, что делятся они лишь на 1 и само себя. До сих пор их изучают учёные по всему миру. Также они применяются в вычислительной технике: с их помощью можно писать алгоритмы, чтобы шифровать данные. Давайте напишем программу, чтобы определять — простое перед нами число или нет.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется вывести сообщение YES если число простое, иначе — NO.

Примечание
Простым называется число, которое имеет ровно два делителя.
"""
number = int(input())
if number == 1:
    print("NO")
else:
    k = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            k += 1
        if k > 1:
            print("NO")
            break
    if k == 1:
        print("YES")
        