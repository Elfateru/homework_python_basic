ip_address = '{0}.{1}.{2}.{3}'
nums_list = []
count = 0
while count < 4:
    num = int(input('Введите число: '))
    if 0 <= num <= 255:
        nums_list.append(num)
        count += 1

print(ip_address.format(*nums_list))
