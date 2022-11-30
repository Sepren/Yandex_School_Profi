"""
Дети продолжают запоминать цифры, а мы им помогать.
Нам вновь называют начало и конец последовательности чисел, а мы выводим их и числа между.

Формат ввода
Два числа, каждое с новой строки.

Формат вывода
Все числа от начала до конца (включительно), записанные через пробел.
"""
start_position, end_position = int(input()), int(input())
if start_position > end_position:
    for i in range(start_position, end_position - 1, -1):
        print(i, end = ' ')
else:
    for i in range(start_position, end_position + 1):
        print(i, end = ' ')