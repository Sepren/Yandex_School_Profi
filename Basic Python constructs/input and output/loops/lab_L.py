"""
Давайте попробуем выполнить ещё одно просто действие — найдём максимальную цифру числа.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется вывести одно натуральное число — максимальную цифру исходного.
"""
number = int(input())
max = 0
while number != 0:
    if max <= number % 10:
        max = number % 10
    number //= 10
print(max)