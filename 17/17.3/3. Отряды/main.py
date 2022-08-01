import random

first_squad = [random.randint(50, 80) for _ in range(10)]
second_squad = [random.randint(30, 60) for _ in range(10)]
third_squad_condition = [('Погиб' if first_squad[i_dmg] + second_squad[i_dmg] > 100
                         else 'Выжил')
                         for i_dmg in range(10)]

print('Урон первого отряда:', first_squad)
print('Урон второго отряда:', second_squad)
print('Состояние третьего отряда:', third_squad_condition)
