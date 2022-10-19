salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


# TODO Оформить решение
def getmoneycount(salary, spend, months, increase):
    need_money = 0
    spend /= 1 + increase
    for iterator in range(months):
        need_money += (1 + increase) * spend - salary
    return need_money


need_money = getmoneycount(salary, spend, months, increase)
print(round(need_money))
