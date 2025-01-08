import math
# exit program
import sys
# sum a and b
def sum(a,b):
    return a + b
# sum multi number
def sumMultiNumbers():
    sum = 0
    quality = int(input("Nhập số lượng số cần tính: "))
    i = 1
    while i <= quality :
        var = int(input(f"Nhập số thứ {i}: "))
        sum += var
        i += 1
    return sum
# isPrime
def isPrime (num):
    if num < 2:
        return False
    for i in range (2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
# isPrime [a,b]
def isPrime2 (a,b):
    for i in range (a, b):
        if(isPrime(i)):
            print(i , end = " ")
#  check perfect number
def perfectNumber(num):
    sum = 0
    check = False
    for i in range (1, num):
        if(num%i==0):
            sum += i
    if(sum == num):
        check = True
    return check
# check perfect number [a,b]
def perfectNumber2 (a,b):
    for i in range (a, b):
        if(perfectNumber(i)):
            print(i , end = " ")
def menu():
    while True:
        print("1. Tính tổng 2 số")
        print("2. Tính tổng 1 dãy số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Kiểm tìm nguyên tố trong khoảng từ a đến b")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Kiểm tìm hoàn hảo trong khoảng từ a đến b")
        print("7. Thoát chương trình")
        select = int(input("Select an option: "))
        if select == 1:
            print(">>> BẠN ĐÃ CHỌN TÍNH TỔNG HAI SỐ <<<")
            a = int(input("Nhập số a: "))
            b = int(input("Nhập số b: "))
            print(f">>> Tổng của {a} và {b}: ",sum(a, b))
        elif select == 2:
            print(">>> BẠN ĐÃ CHỌN TÍNH TỔNG 1 DÃY SỐ <<<")
            res = sumMultiNumbers()
            print(">>>Tổng của dãy số vừa nhập là: ",res)
        elif select == 3:
            print(">>> BẠN ĐÃ CHỌN KIỂM TRA SỐ NGUYÊN TỐ <<<")
            n = int(input("Nhập số cần kiểm tra: "))
            res = isPrime(n)
            if res:
                print(">>>",n, "là số nguyên tố")
            else:
                print(">>>",n, "không là số nguyên tố")
        elif select == 4:
            print(">>> BẠN ĐÃ CHỌN TÌM SỐ NGUYÊN TỐ [A,B] <<<")
            number1 = int(input("Nhập số thứ nhất: "))
            number2 = int(input("Nhập số thứ hai:"))
            print(f">>> Các số nguyên tố trong khoảng từ {number1} đến {number2} là:")
            isPrime2(number1, number2)
            print("\n")
        elif select == 5:
            print(">>> BẠN ĐÃ CHỌN KIỂM TRA SỐ HOÀN HẢO <<<")
            n = int(input("Nhập số cần kiểm tra: "))
            res = perfectNumber(n)
            if res:
                print(">>>",n,"là số hoàn hảo")
            else:
                print(">>>",n,"không là số hoàn hảo")
        elif select == 6:
            print(">>> BẠN ĐÃ CHỌN TÌM SỐ HOÀN HẢO TRONG KHOẢNG [A,B] <<<")
            number1 = int(input("Nhập số thứ nhất: "))
            number2 = int(input("Nhập số thứ hai:"))
            print(f">>> Các số hoàn hảo trong khoảng từ {number1} đến {number2} là:")
            perfectNumber2(number1, number2)
            print("\n")
        elif select == 7:
            exit(0)
        else:
            print(">>> Bạn chọn không đúng <<<")
menu()


