# Nhập chuỗi các số nhị phân từ bàn phím
binary_string = input("Nhập chuỗi các số nhị phân, phân tách bởi dấu phẩy: ")

# Tách thành các số nhị phân
binary_numbers = binary_string.split(',')

# Danh sách để lưu các số nhị phân chia hết cho 5
result = []

# Kiểm tra từng số nhị phân
for binary in binary_numbers:
    if int(binary, 2) % 5 == 0:
        result.append(binary)

# In các số nhị phân chia hết cho 5
print(",".join(result))
