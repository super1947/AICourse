# generateList.py

kim = ['김유신', 10, 20]
lee = ['이순신', 30, 40]
park = ['박지성', 50, 60]
student = [kim, lee, park]

mylist = list()
for sublist in student:
    mylist.append([sublist[0], sublist[1]+sublist[2]])

print(mylist)
