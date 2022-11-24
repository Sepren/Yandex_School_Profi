"""
Существуют такое интересное понятие как палиндром — число, слово, предложение и так далее, которое и слева-направо, и справа-налево читается одинаково.

Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода
Одно четырёхзначное число

Формат вывода
YES если число является палиндромом, иначе — NO.
"""

number = int(input())
if str(number) == str(number)[::-1]:
    print("YES")
else:
    print("NO")