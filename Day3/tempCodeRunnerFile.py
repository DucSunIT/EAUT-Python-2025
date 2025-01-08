def kiemTraSoHoanHao(n):
    sum = 0
    for i in range (1,n):
        if(n % i ==0):
            sum += i
    if(sum == n):
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không là số hoàn hảo")
n = int(input("Nhập n = "))
kiemTraSoHoanHao(n)