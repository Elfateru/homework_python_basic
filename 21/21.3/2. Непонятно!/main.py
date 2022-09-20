def data_chech(data, obj, mut_check):
    data_type = type(obj)
    print(data_type)
    data_name = data[str(data_type)]
    print('Тип данных:', data_name)
    if data_type in mut_check['mutable']:
        print('Изменяемый (mutable)')
    else:
        print('Неизменяемый (immutable)')
    print('Id объекта:', id(obj))

data_names_dict = {
    "<class 'str'>": "str (строка)",
    "<class 'dict'>": "dict (словарь)",
    "<class 'list'>": "list (список)",
    "<class 'set'>": "set (множество)",
    "<class 'int'>": "int (число)",
    "<class 'float'>": "float (число с плавающей точкой)",
    "<class 'tuple'>": "tuple (кортеж)",
    "<class 'bool'>": "bool (булево значение)"
}

mutable_check = {
    'mutable': ("<class 'dict'>", "<class 'list'>", "<class 'set'>")
}

data_input = {'a': 10, 'b': 20}

data_chech(data_names_dict, data_input, mutable_check)
