_number = int(input("Nhap so nguyen duong: "))
if _number < 0:
    print("Nhap so lon hon khong")
else:
    if (_number % 2==0 and _number %3==0):
        print(f"{_number} chia het co ca 2 va 3")
    elif (_number % 2 == 0):
        print(f"{_number} chia het cho 2")
    elif (_number % 3 == 0):
        print(f"{_number} chia het cho 3")
    else:
        print(f"{_number} khong hop le")
    
