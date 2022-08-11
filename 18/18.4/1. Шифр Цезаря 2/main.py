print(ord("а"), ord("я"), ord("ё"), chr(1104))

alphabet = ''.join([chr(index) if index != 1077 else chr(index) + chr(1105)
                    for index in range(ord("а"), ord("я") + 1)])
text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))
caesar_cipher = ''.join([alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
                         if sym in alphabet else sym
                         for sym in text.lower()])

print(caesar_cipher)
