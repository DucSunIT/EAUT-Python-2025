
def checkInt(n):
    if n > 10:
        print("So nhap vao phai < 10")
    else:
        for i in range(n + 1):
            if i % 2 == 0:
                print(i, end=" ")
    return
n = int(input("Nhap n = "))
checkInt(n)
