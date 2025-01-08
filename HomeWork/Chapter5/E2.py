import os
res = 'test.txt'
file = open(res, 'r+', encoding='utf-8')
# di chuyển con trỏ đến cuối file
file.seek(0, os.SEEK_END)
n = str(input("Nhập dữ liệu cần ghi: "))
res = file.write(n + "\n")
# quay lại đầu file để đọc
file.seek(0, os.SEEK_SET)
lines = file.readlines()
# dùng index âm để lấy từ cuối danh sách
print("Nội dung vừa ghi là: " , lines[-1].strip())

file.close()