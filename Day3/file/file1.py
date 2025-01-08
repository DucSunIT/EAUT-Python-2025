import os
# encoding="utf-8" ghi tieng viet co dau
file = open("D:/EAUT/Junior/Python/Day3/file/test.txt", "r+", encoding="utf-8")
# read doc toan bo file
# str = file.read()
a = file.readline()
b = file.readline()
c = int(a) + int(b)
print("Write sucesfully!!")
# ghi file
file.write("\n" + str(c))

# close file
file.close()
