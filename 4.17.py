
n = int(input("Nhập số n: "))

def sum_of_divisors(x):
    return sum(i for i in range(1, x) if x % i == 0)

for num in range(1, n):
    if sum_of_divisors(num) > num:
        print(num)
