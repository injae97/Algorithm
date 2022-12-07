def solution(strlist):
    arr = []
    for i in strlist:
        arr.append(len(i))

    return arr

# --------- input ------------
strlist = ["We", "are", "the", "world!"]
print(solution(strlist))