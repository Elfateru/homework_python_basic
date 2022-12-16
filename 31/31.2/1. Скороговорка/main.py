import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match('wo', text)
print('Поиск шаблона в начале строки:', result)
result = re.search('wo', text)
print('Поиск первого найденного совпадения по шаблону:', result)
print('Содержимое найденной подстроки:', result.group(0))
result_1 = result.start()
print("Начальная позиция:", result_1)
result_1 = result.end()
print("Конечная позиция:", result_1)
result_1 = re.findall('wo', text)
print('Список всех упоминаний шаблона:', result_1)
result_1 = re.sub('wo', 'ЗАМЕНА', text)
print('Текст после замены:', result_1)
