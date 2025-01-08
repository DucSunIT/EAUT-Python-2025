import math
n = int(input("Nhap n: "))
check = 1
if(n < 2):
    check = 0
    print(f"{n} khong phai la so nguyen to")
else:
    for i in range (2, n):
        if(n % i ==0):
            print(f"{n} khong phai la so nguyen to")
            check = 0
            break;
if(check):
    print(f"{n} la so nguyen to")
        