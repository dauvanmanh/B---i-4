full_name = input('Nhập tên đầy đủ: ')

name_parts = full_name.split()

ho = name_parts[0]
ten = name_parts[-1]

print("Họ:", ho)
print("Tên:", ten)
