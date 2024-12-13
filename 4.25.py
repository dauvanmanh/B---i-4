# Nhập danh sách các số từ bàn phím, cách nhau bởi dấu phẩy
numbers = input("Nhập danh sách các số: ").split(',')

# Lọc các số lẻ
odd_numbers = [num for num in numbers if int(num) % 2 != 0]

# In các số lẻ
print(",".join(odd_numbers))
