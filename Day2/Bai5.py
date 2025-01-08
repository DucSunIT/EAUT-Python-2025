import math
a = float(input("Nhap so hang a: "))
b = float(input("Nhap so hang b: "))
c = float(input("Nhap so hang c: "))
# if (a==b==c==0)
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c / b
        print(f"Nghiem cua phuong trinh la: {x}")
else:
    delta = math.pow(b,2) - 4 * a * c
    if(delta < 0 ):
        print("Phuong trinh vo nghiem")
    elif (delta == 0):
        x = -b / (2*a)
        print(f"Phuong trinh co nghiem kep  x1 = x2 = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phuong trinh co 2 nghiem phan biet x1 = {x1}, x2 = {x2}")

