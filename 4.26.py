# Khởi tạo biến lưu số tiền thực trong tài khoản
balance = 0

# Nhập nhật ký giao dịch
while True:
    transaction = input()
    if not transaction:
        break
    type, amount = transaction.split()
    amount = int(amount)
    
    if type == 'D':
        balance += amount
    elif type == 'W':
        balance -= amount

# In số tiền thực trong tài khoản
print(balance)
