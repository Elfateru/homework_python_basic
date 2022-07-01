def is_film_exist(movie, film_list):
    for i_movie in film_list:
        if i_movie == movie:
            return True
    return False


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_films_list = []

while True:
    print('Ваш текущий топ фильмов:', my_films_list)
    new_movie = input('Название фильма: ')
    if is_film_exist(new_movie, films):  #Проверяем есть ли фильм в общем списке
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            if is_film_exist(new_movie, my_films_list):  #Проверяем наличие фильма в нашем списке
                print('Этот фильм уже есть в вашем списке')
            else:
                my_films_list.append(new_movie)
        if command == 'удалить':
            if is_film_exist(new_movie, my_films_list):  #Проверяем наличие фильма в нашем списке
                my_films_list.remove(new_movie)
            else:
                print('Такого фильма нет в вашем списке')
        if command == 'вставить':
            index = int(input('На какое место? '))
            if len(my_films_list) >= index - 1:
                my_films_list.insert(index - 1, new_movie)
            else:
                print('Ваш список слишком мал для такого индекса места списка')
    else:
        print('Такого фильма нет в нашем списке')
