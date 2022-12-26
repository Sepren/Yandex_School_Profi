"""
Во многих играх порядок ходов определяется броском кубика или монетки, а в нашей первым ходит тот, чье имя лексикографически меньше. Определите, кто из игроков будет ходить первым.

Формат ввода
В первой строке записано одно натуральное число NN — количество игроков.
В каждой из последующих NN строк указано одно имя игрока.

Формат вывода
Имя игрока, который будет ходить первым.
"""
quantity = int(input())
name = input()
max = name
for i in range(quantity - 1):
    name = input()
    if name <= max:
        max = name
print(max)