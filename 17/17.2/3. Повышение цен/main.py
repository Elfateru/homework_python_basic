def new_price(percent, price):
    return round(price * (1 + percent / 100), 2)


price_now = [float(input('Цена на товар: ')) for _ in range(5)]

first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

price_first = [new_price(first_percent, i_price) for i_price in price_now]
price_second = [new_price(second_percent, i_price) for i_price in price_first]

print('Сумма цен за каждый год:', round(sum(price_now), 2), round(sum(price_first), 2), round(sum(price_second), 2))

