money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


# TODO Оформить решение
def getlifetime(money_capital, salary, spend, increase):
    counter = 0
    while money_capital > 0:
        money_capital += salary - (1 + increase) * spend
        counter += 1
    return counter


month = getlifetime(money_capital, salary, spend, increase)
print(month)
