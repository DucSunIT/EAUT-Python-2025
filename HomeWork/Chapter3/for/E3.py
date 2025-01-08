
def divFiveOrSeven(num):
    if num >= 20:
        print("So nhap vao < 20")
    else:
        for i in range (1, num):
            if i % 5 == 0 or i % 7 == 0:
                print(i, end = " ")
    return
n = int(input("Nhap n = "))
divFiveOrSeven(n)