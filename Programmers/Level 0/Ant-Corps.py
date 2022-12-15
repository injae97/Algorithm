def solution(hp):
    # // 연산자는 나눌 수 없을 경우 return 0
    general_ant = hp // 5
    general_ant_r = hp % 5
    soldier_ant = general_ant_r // 3
    worket_ant = general_ant_r % 3 # worket_ant = 1 이므로 general_ant_r % 3 값을 구하면 된다

    return general_ant + soldier_ant + worket_ant

def solution2(hp):
    answer = 0
    for ant in [5, 3, 1]:
        quotient, hp = divmod(hp, ant) # divmod(num1, num2) : num1을 num2로 나눈 몫(quotient)과 나머지(hp)를 출력
        answer += quotient

    return answer

# --------- input ------------
hp = 9
print(solution(hp))