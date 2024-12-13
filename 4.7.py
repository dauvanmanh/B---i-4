chuoi = input('Nhập chuỗi: ')

chuoi_khong_so = ''.join([ch for ch in chuoi if not ch.isdigit()])

print(chuoi_khong_so)
