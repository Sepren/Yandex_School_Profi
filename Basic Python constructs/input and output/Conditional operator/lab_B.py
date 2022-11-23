"""
В главной велогонке года участвует более тысячи гонщиков. Им предстоит пройти трассу длинной 43872м. Самая сложная и ответственная задача — определение победителя.

Нам известны средние скорости двух фаворитов — Пети и Васи. Помогите выяснить, кто из них пришёл к финишу первым.

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.

Формат вывода
Имя победителя гонки.

Примечание
Гарантируется, что победителем стал только один.
"""

petya_speed, vasia_speed = int(input()), int(input())
if petya_speed > vasia_speed:
    print("Петя")
else:
    print("Вася")