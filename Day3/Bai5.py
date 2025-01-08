def kiemTraSoHoanHao(n):
    sum = 0
    # i sẽ chạy từ 1 đến sất n (<n)
    for i in range (1,n):
        if(n % i ==0):
            print(i, end=" ")
            sum += i
    if(sum == n):
        print(f"\n{n} là số hoàn hảo")
    else:
        print(f"\n{n} không là số hoàn hảo")
n = int(input("Nhập n = "))
kiemTraSoHoanHao(n)
# 6 {1,2,3} = 1 + 2 + 3 = 6 