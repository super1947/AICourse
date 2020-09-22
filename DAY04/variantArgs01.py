# variantArgs01.py
# 가변 인자 : * 기호가 매개변수로 사용되면 tuple로 인식이 된다.

def func(*args):
  total = 0
  for item in args:
    total += item
  print(f'총합 : {total}')

func(1)
func(5, 6, 7)
func(1,3,4,6,2,3,4,2,5,6,2)