import math
def isPrime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def timSoNguyenToTrongKhoang(a,b):
    # i sẽ chạy từ i = a đến b (<=b)
    count = 0
    for i in range(a,b+1): 
        if(isPrime(i)):
            print(i , end=" ")
            count += 1
    return count

number1 = int(input("Nhâp số đầu: "))
number2 = int(input("Nhập số cuối: "))
print(f">>> Các số nguyên tố từ khoảng {number1} đến {number2} là:")
countSNT = timSoNguyenToTrongKhoang(number1,number2)
print(f"\n>>> Có {countSNT} số nguyên tố trong khoảng từ {number1} đến {number2}")