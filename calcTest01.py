result = 0
def calc(num):
    global result
    result += num
    return result

print(calc(3))
print(calc(4))