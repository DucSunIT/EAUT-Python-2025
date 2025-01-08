# def sum(a,b):
#     return a + b

# print(sum(2,3))

def sumNumbers(*var):
    sum = 0
    for i in var:
        sum += i
        # không làm gì cả, sẽ bỏ qua giúp chương trình không lỗi
        # pass 
    return sum
print(sumNumbers(9,8,7,6,5,4,3,2,1))