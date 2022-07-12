zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
for index in range(len(zoo)):
    if zoo[index] == 'lion':
        zoo.insert(index + 1, 'bear')
zoo.remove('elephant')

print('Зоопарк:', zoo)
print('\nЛев сидит в клетке номер', zoo.index('lion') + 1)
print('\nОбезьяна сидит в клетке номер', zoo.index('monkey') + 1)