# Nhập danh sách từ bàn phím, các từ cách nhau bởi dấu cách hoặc tab
ds = input('Nhập danh sách: ').split()

# Tìm từ dài nhất trong dãy
max_length = max(len(word) for word in ds)
longest_words = [word for word in ds if len(word) == max_length]

# In từ dài nhất và tất cả các từ có cùng độ dài
print("Từ dài nhất:", ', '.join(longest_words))
