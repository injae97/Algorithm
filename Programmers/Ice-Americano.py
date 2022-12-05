def solution(money):
    coffee = 5500
    return [money // coffee, money % coffee]

# --------- input ------------
money = 5500
print(solution(money))