num_str = "0123456789"

# 截取 2-5 位置的字符串
num_str[2:6]

# 截取 2-末尾的字符串
num_str[2:]

#截取开始到5的字符串
num_str[0:6]
num_str[:6]

# 截取完整的字符串
num_str[:]

# 从开始位置，每隔一个字符截取字符串
num_str[::2]

#从索引1开始，每隔一个取一个
print(num_str[1::2])

#截取从2-末尾 -1的字符串
num_str[2:-1]

#截取字符串末尾两个字符串
num_str[-2:]

#字符串的逆序
num_str[-1::-1]
num_str[::-1]