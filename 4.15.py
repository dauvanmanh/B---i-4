
input_string = input("Nhập các từ tiếng Anh: ")

words = input_string.split()

words.sort()

for word in words:
    print(word)
