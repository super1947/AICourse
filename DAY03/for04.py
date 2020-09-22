# tuple을 저장하고 있는 list 자료 구조

examdata = [(50, 70), (60, 75), (55, 80)]
#         [0][0]     [1][0]        [2][1]

for (midexam, finalexam) in examdata:
    print(f'중간 고사 : {midexam}, 기말 고사 : {finalexam}')

print('고사별 총합 구해 보기')
midsum = finalsum = 0
for (midexam, finalexam) in examdata:
    midsum += midexam
    finalsum += finalexam
print(f'중간 총합 : {midsum}, 기말 총합 : {finalsum}')
print(examdata[1][1])

firstsum = lastsum = 0
print('인덱싱과 range()함수를 사용하여 고사별 총합 구해 보기')
for idx in range(len(examdata)):
    firstsum += examdata[idx][0]
    lastsum += examdata[idx][1]
print(f'중간 총합 : {firstsum}, 기말 총합 : {lastsum}')
