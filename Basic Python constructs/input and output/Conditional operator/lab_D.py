"""
Длинна трассы — 43872м, а зрители хотят узнать имя победителя.

Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Имена победителей в порядке занятых мест.
"""

Petya_speed, Vasia_speed, Tolya_speed = int(input()), int(input()), int(input())

if Petya_speed > Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed > Vasia_speed:
    print("""1. Петя\n2. Толя\n3. Вася""")
elif Petya_speed > Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed < Vasia_speed:
    print("""1. Петя\n2. Вася\n3. Толя""")
elif Petya_speed > Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed > Vasia_speed:
    print("""1. Толя\n2. Петя\n3. Вася""")
elif Petya_speed < Vasia_speed and Petya_speed > Tolya_speed and Tolya_speed < Vasia_speed:
    print("""1. Вася\n2. Петя\n3. Толя""")
elif Petya_speed < Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed > Vasia_speed:
    print("""1. Толя\n2. Вася\n3. Петя""")
elif Petya_speed < Vasia_speed and Petya_speed < Tolya_speed and Tolya_speed < Vasia_speed:
    print("""1. Вася\n2. Толя\n3. Петя""")