"""
В продуктовом магазине объявили акцию: «На все товары с ценой не менее 500 тугриков предоставляется скидка 10%».
Нас попросили разработать программное обеспечение кассового автомата, которое будет считать итоговую сумму покупки с учётом скидки.

Формат ввода
Вводится некоторое количество рациональных чисел — стоимость товаров.
Список завершается значением 0.

Формат вывода
Требуется вывести сумму всех товаров с учётом объявленной акции.
"""

sum = 0
while (price := int(input())) != 0:
    if price >= 500:
        sum += price * 0.9
    else:
        sum += price
print(sum)