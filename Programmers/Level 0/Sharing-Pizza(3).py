def solution(slice, n):
    if n % slice == 0:
        return n // slice 
    else :
        return n // slice + 1

# --------- input ------------
slice, n = 7, 10
print(solution(slice, n))