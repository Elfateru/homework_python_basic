while True:
    grats_template = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    else:
        print('Отсутствует одна или две конструкции!')

names_list = input('Введите имена и фамилии через запятую с пробелом:').split(', ')
ages_str = input('Введите возраст через пробел: ')
ages_list = [int(num) for num in ages_str.split()]

for index, name in enumerate(names_list):
    print(grats_template.format(name=name, age=ages_list[index]))

print("Именинники:", ", ".join([' '.join([names_list[index], str(ages_list[index])])
                               for index in range(len(names_list))]))
