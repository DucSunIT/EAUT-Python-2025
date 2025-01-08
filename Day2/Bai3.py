import time
_namsinh = int(input("Nhap nam sinh: "))
# lay thoi gian hien tai
current_year = time.localtime()
# print(current_year)
if(_namsinh <= 0 or _namsinh > current_year.tm_year):
    print("Nhap sai nam sinh")
else:
    print("Tuoi cua may la: ", current_year.tm_year - _namsinh)
