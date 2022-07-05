pack = []
decode = []
bad_packs = 0

packs_amount = int(input('Кол-во пакетов: '))

for i_pack in range(packs_amount):
    print('\nПакет номер', i_pack + 1)
    for bit in range(4):
        print(bit + 1, 'бит: ', end='')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете')
        bad_packs += 1
    pack = []

print('Полученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)
