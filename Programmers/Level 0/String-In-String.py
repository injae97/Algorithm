def solution(str1, str2):
    return 1 if str2 in str1 else 2

# --------- input ------------
str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"
print(solution(str1, str2))