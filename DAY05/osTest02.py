# osTest02.py
# os 모듈 : Operating System(운영체제)와 관련된 모듈
# 폴더 생성, 수정, 삭제 등등
# 파일과 관련된 여러 가지 속성 정보
import os
# 폴더 구분자를 사용할 때 /는 한번만, \는 반드시 두개 ex) c:/user, c:\\user
myfolder = 'd:\\'
newpath = os.path.join(myfolder, 'sample')

try:
    os.mkdir(path=newpath) # mkdir : make directory
    for i in range(1, 11):
        newfile = os.path.join(newpath, 'folder' + str(i).zfill(2))
        os.mkdir(path=newfile)
except FileExistsError as err:
    print(err)

print('#'*30)