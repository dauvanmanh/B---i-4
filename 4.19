def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Tạo danh sách các số nguyên tố nhỏ hơn 1 triệu
prime_numbers = [x for x in range(2, 1000000) if is_prime(x)]

# Chuyển danh sách thành tuple
P = tuple(prime_numbers)

# In tuple P
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:", P)
