"""
В задачнике ко второй лекции мы помогали детям искать зайца.
На этот раз мы будем искать и считать сразу нескольких зайчат.

Формат ввода
Вводятся строки, описывающие придорожную местность.
В конце поездки вводится «Приехали!»

Формат вывода
Количество строк, в которых есть зайка.
"""
find_word = 'зайка'
quantity = 0
while (name := input()) != "Приехали!":
    if find_word in name:
        quantity += 1
print(quantity)