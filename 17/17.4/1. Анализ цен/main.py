import random

original_prices = [random.randint(-12, 10) for _ in range(5)]

new_prices = [price if price > 0 else 0 for price in original_prices]
print("Мы потеряли: ",  sum(new_prices) - sum(original_prices))
