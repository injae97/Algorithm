def solution(price):
    if 0 <= price <= 99999:
        return price

    elif 100000 <= price <= 299999:
        return int(price - (price * 0.05))

    elif 300000 <= price <= 499999:
        return int(price - (price * 0.1))

    elif 500000 <= price:
        return int(price - (price * 0.2))

# --------- input ------------
price = 150000
print(solution(price))