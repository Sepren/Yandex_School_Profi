"""
Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.

На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Имя победителя гонки.

Примечание
Гарантируется, что победителем стал только один.
"""

petya_speed, vasia_speed, tolya_speed = int(input()), int(input()), int(input())
if petya_speed > vasia_speed and petya_speed > tolya_speed:
    print("Петя")
elif tolya_speed > vasia_speed and petya_speed < tolya_speed:
    print("Толя")
elif petya_speed < vasia_speed and vasia_speed > tolya_speed:
    print("Вася")
