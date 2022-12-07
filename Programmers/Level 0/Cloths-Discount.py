def solution(price):
    if 100000 <= price <= 299999:
        price = price - (price * 0.05)

    elif 300000 <= price <= 499999:
        price = price - (price * 0.1)

    elif 500000 <= price:
        price = price - (price * 0.2)

    return int(price)

def solution2(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

# --------- input ------------
price = 150000
print(solution2(price))