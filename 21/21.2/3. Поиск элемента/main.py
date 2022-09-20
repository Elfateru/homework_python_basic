def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            rusult = find_key(sub_struct, key)
            if rusult:
                break
    else:
        rusult = None
    return rusult


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Искомый ключ: ')

value = find_key(site, user_key)
if value:
    print('Значение:', value)
else:
    print('Такого ключа в структуре сайта нет.')
