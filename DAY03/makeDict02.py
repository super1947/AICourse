# makeDict02.py
# fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30)]
mydict = dict()  # empty dict
print(mydict)

# for key, value in fruits:
#   mydict[key] = value
#
# print(mydict)

fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30), ('바나나', 50)]

for key, value in fruits:
    if not key in mydict:
        mydict[key] = value
    else:
        temp = mydict[key]
        mydict[key] = temp + value
print(mydict)
print('바나나' in mydict)
