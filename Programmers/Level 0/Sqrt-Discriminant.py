def solution(n):
    # e.g n:144 = float (12.0 == 12) return 1, n:976 (31.240998703626616 != 31) return 2
    if n ** 0.5 == int(n ** 0.5):
        return 1
    else:
        return 2

# --------- input ------------
n = 976
print(solution(n))