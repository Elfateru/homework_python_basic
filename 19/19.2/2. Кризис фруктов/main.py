incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

min_value = None
min_name = ''
for name, val in incomes.items():
    if min_value is None or min_value > val:
        min_value = val
        min_name = name

print('Общий доход за год составил', sum(incomes.values()))
incomes.pop(min_name)
print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(min_name, min_value))
print('Итоговый словарь: ', incomes)
