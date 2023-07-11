import random
import time
# seed 를 고정
# random.seed(41)
# seed 가 고정되어서 항상 같은 값이 나옴

# 1 ~ 45 중 랜덤하게 6개 숫자를 랜덤하게 선정
range45 = range(1, 46)
result = random.sample(range45, 6)
list(result)
result.sort()

answer = [1, 5, 10, 23, 35, 39]

cnt = 0
cntnot = 0

# answer 과 비교하고 일치하면 카운트 증가
for index in range(0, len(answer)):
    if(result[index] == answer[index]):
        cnt = cnt + 1
    else:
        cntnot = cntnot + 1

print(result, answer, cnt, cntnot, sep="\n")

