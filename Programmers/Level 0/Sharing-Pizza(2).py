def solution(n):
    pizza = 6
    while pizza % n != 0:
        pizza += 6

    return int(pizza / 6)

# --------- input ------------
n = 6
print(solution(n))