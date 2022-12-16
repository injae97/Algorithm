def solution(rsp):
    scissors, rock, paper = "2", "0", "5"
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == scissors:
            answer += "0"
        elif rsp[i] == rock:
            answer += "5"
        else:
            answer += "2"

    return answer

def solution2(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

# --------- input ------------
rsp = "205"
print(solution(rsp))