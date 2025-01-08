import math
def isPrime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def timSoNguyenToTrongKhoang(a,b):
    for i in range(a,b):
        if(isPrime(i)):
            print(f"{i} ")
    return

timSoNguyenToTrongKhoang(10,50)
n = int(input("Nhập n = "))
if(isPrime(n)):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
