
def multiTenNumbers(num):
    t = 1
    i = 1
    while i <= num:
        t *= i
        i += 1
    return t
n = int(input("Nhap n so tu nhien: "))
multiple = multiTenNumbers(n)
print(multiple)