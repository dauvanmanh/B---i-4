# Danh sách để lưu các số thỏa mãn điều kiện
result = []

# Kiểm tra từng số trong đoạn từ 1000 đến 3000
for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num_str)

# In các số tìm được
print(",".join(result))
