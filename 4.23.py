# Nhập câu từ bàn phím
sentence = input("Nhập câu: ")

# Khởi tạo biến đếm
letters = 0
digits = 0

# Kiểm tra từng ký tự trong câu
for ch in sentence:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# In kết quả
print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
