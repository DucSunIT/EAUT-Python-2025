# for _i in range(80,100):
#     if (_i % 2 == 0 and _i % 3 ==0):
#         print(_i)

count = 0
while count <= 3:
    print("Dang o trong while ", count)
    count+=1
    if(count % 2 ==0):
        break
else:
    print("Dang o trong else")
print("Dang o ngoai while")