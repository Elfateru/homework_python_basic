string = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')
print()

dbl_sym = [sym * 2 for sym in string]
add_dbl_sym = [sym + symbol for sym in dbl_sym]

print('Список удвоенных символов:', dbl_sym)
print('Склейка с дополнительным символом:', add_dbl_sym)
