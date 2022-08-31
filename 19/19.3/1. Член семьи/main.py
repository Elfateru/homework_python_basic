family_member = {
    'name': 'Jane',
    'surname': 'Doe',
    'hobbies': ['running', 'sky diving', 'singing'],
    'age': 35,
    'children': [
        {
            'name': 'Alice',
            'age': 6
        },
        {
            'name': 'Bob',
            'age': 8
        }
    ]
}

children_dict = {}
for child in family_member['children']:
    children_dict[child['name']] = child['age']

search_Bob = children_dict.get('Bob', None)
if search_Bob:
    print('Bob найден')
else:
    print('Bob-a нет!')

children_surname = family_member.get('surname', None)
if children_surname:
    print(children_surname)
else:
    print('Nosurname')