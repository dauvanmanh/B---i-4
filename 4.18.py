# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))

# Hàm tạo danh sách các số Fibonacci nhỏ hơn n
def fibonacci_less_than(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Tạo và in danh sách các số Fibonacci nhỏ hơn n
fibonacci_list = fibonacci_less_than(n)
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_list)
