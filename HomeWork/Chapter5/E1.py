import os
res = 'test.txt'
file = open(res, 'r+', encoding='utf-8')
n = int(input("Nhap so dong: "))
count = 0
for line in file:
    if count >= n:
        break
    print(line.strip())
    count += 1
file.close()