goods = [["яблоки", 50], ["апельсины", 190],
         ["груши", 100], ["нектарины", 200],
         ["бананы", 77]]

print('Текущий ассортимент:', goods)

fruit = input('\nНовый фрукт: ')
price = int(input('Цена: '))
new_goods = []
new_goods.append(fruit)
new_goods.append(price)

goods.append(new_goods)
print('\nНовый ассортимент:', goods)

for i_index in range(len(goods)):
    goods[i_index][1] += goods[i_index][1] * 8 / 100

print('\nНовый ассортимент с увел. ценой:', goods)