mylist = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(len(mylist))

# 집합 : 중복을 허락하지 않는 자료 구조
# 관련 함수 : set()
# 특징 : 합집합, 교집합, 차집합 등의 함수를 제공합니다.
# 집합은 {}로 이루어져 있음
# 중복을 제거하고 싶을 때 잠깐 set()으로 집합으로 바꿨다가
# 다시 list()로 리스트로 바꾸는 경우가 많음.
# 함수 : add(), update(), remove()

myset = set(mylist)
print(myset)
print(len(myset))

newlist = list(myset)
print(newlist)

set1 = set([1, 2, 3])
print(set1)

set1.add(4)
print(set1)

set1.update(([5, 6, 7]))
print(set1)

set1.remove(4)
print(set1)

set3 = set([1, 2, 3, 4])
set4 = set([3, 4, 5, 6])

set5 = set3.intersection(set4)
print(set5)

set6 = set3.union(set4)
print(set6)

set7 = set3.difference(set4)
print(set7)

set8 = set4.difference(set3)
print(set8)

# 차집합은 교환 법칙이 성립하지 않는다.
# -> set3 - set4 != set4 - set3


# 다음은 어떤 자료 구조로 표현하면 좋을까요?
# 1) 회원가입 정보 (ID : 'hong', 이름은 '홍길동') -> dict
# 2) 로또 번호 생성기 -> set
# 3) 게시물의 제목 정보 -> list