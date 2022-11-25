from math import *
a, b, c = float(input()), float(input()), float(input())
if a == 0 and b == 0 and c == 0 or a != 0 and b == 0 and c == 0 or a == 0 and b != 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    print(-c / b)
elif a != 0 and b == 0 and c != 0:
    print(min(-sqrt(-c/a), sqrt(c/a)), max(-sqrt(-c/a), sqrt(c/a)))
elif a != 0 and b != 0 and c == 0:
    print(min(0, -b / a), max(0, -b / a))
elif a == 0 and b == 0 and c != 0:
    print("No solution")
else:
    D = b * b - 4 * a * c
    if sqrt(D) < 0:
        print("No solution")
    elif sqrt(D) == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(min(x1, x2), max(x1, x2))