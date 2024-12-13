# Nhập câu từ bàn phím
sentence = input("Nhập câu: ")

# Khởi tạo biến đếm
upper_case = 0
lower_case = 0

# Kiểm tra từng ký tự trong câu
for ch in sentence:
    if ch.isupper():
        upper_case += 1
    elif ch.islower():
        lower_case += 1

# In kết quả
print("Chữ hoa:", upper_case)
print("Chữ thường:", lower_case)
