"""
Вася любит полениться. Особенно ему нравится, когда в году появляется такой лишний денёк, которого обычно не бывает. Напишите программу, которая поможет Васе определить, удастся ли ему побездельничать в определённом году или нет.

Формат ввода
Одно число — год.

Формат вывода
Одно слово «YES» (удастся) или «NO» (не удастся).
"""

leap_year = int(input())
if leap_year % 100 != 0 and leap_year % 4 == 0 or leap_year % 400 == 0:
    print("YES")
else:
    print("NO")