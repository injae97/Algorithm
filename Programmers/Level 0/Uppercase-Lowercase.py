def solution(my_string):
    answer = ""
    arr = list(map(str, str(my_string)))
    for i in range(len(arr)):
        if arr[i].islower():
            answer += arr[i].upper()
        else :
            answer += arr[i].lower()

    return answer

# --------- input ------------
my_string = "cccCCC"
print(solution(my_string))