def checkCondition(num):
    sum = 0
    i = 1
    while i <= num:
        sum += i
        if sum < num and sum % 2 == 0:
            print(sum, end = " ")
        i += 1
    return
n = int(input("Nhap n = "))
checkCondition(n)
