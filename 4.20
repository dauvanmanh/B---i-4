# Nhập số n từ bàn phím
n = int(input("Nhập số dòng của tam giác Pascal: "))

def generate_pascals_triangle(n):
    result = []
    for i in range(n):
        row = [1]
        if i > 0:
            last_row = result[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        result.append(row)
    return result

# In n dòng đầu tiên của tam giác Pascal
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)
