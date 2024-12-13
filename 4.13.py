# Nhập danh sách từ bàn phím
ds = input('Nhập danh sách: ').split()

# Tìm kiếm phần tử 'abc' trong danh sách
try:
    print("Vị trí của chuỗi 'abc' là", ds.index('abc'))
except ValueError:
    print("Phần tử 'abc' không có trong danh sách")
