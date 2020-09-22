# dictControl.py
# 100번 반복, 매번 1부터 10사이의 임의의 수를 추출, 이것을 사전에 담고, 최종 결과 출력
# 출력 결과 예시 : 숫자 1은 12번 추출, 숫자 2는 5번 추출...숫자 10은 4번 추출

import random
rand_dict = {}

for rand_num in range(1, 100):
    rand_num = random.randint(1, 10)
    if rand_num in rand_dict:
        rand_dict[rand_num] += 1
    else:
        rand_dict[rand_num] = 1

print(rand_dict)

rand_list = [key for key in rand_dict.keys()]
rand_list.sort()

for key in rand_list:
    print(f'숫자 {key}는 {rand_dict[key]}번 추출')