import re

text = 'Eve1n if they are djinns, I will get djinns that can outdjinn them.'

vowel_pattern = r'\b[aAeEiIoOyYuU]\w*'
res = re.findall(vowel_pattern, text)
print('Слова на гласную:', res)
res_2 = re.findall(r'\b[^aAeEiIoOyYuU\W]\w*', text)
print('Слова на любой символ, кроме гласной:', res_2)
