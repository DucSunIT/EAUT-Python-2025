_a = int(input("Nhap a = "))
_b = int(input("Nhap b = "))
_c = int(input("Nhap c = "))
if _a > 0 and _b > 0 and _c > 0:
    if _a + _b > _c and _b + _c > _a and _a + _c > _b :
        print("Day la 3 canh tam giac ")
    else:
        print("Khong phai 3 canh tam giac")
else:
    print("Cac canh phai lon hon 0")

# _a = int(input("Nhập vào a: "))
# _b = int(input("Nhập vào b: "))
# _c = int(input("Nhập vào c: "))

# if _a > 0 and _b > 0 and _c > 0:
#     if _a + _b > _c and _b + _c > _a and _a + _c > _b:
#         print("Đây là 3 cạnh của tam giác")
#     else:
#         print("Đây không phải 3 cạnh của tam giác")
# else:
#     print("Các cạnh phải lớn hơn 0")
