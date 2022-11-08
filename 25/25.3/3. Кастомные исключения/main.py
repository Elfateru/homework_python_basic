class DivissionError(Exception):
    pass


with open('numbers.txt', 'r') as file:
    for line in file:
        try:
            clear_line = line.rstrip()
            f, s = clear_line.split()
            if int(f) < int(s):
                raise DivissionError('Нельзя делить большее на меньшее')
        except (ValueError, DivissionError) as exc:
            print(exc, type(exc), f, s)
