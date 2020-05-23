poem_str = "登鹳雀楼\t,王之涣\t,白日依山尽\t\n, 黄河入海流\t\t,欲穷千里目, 更上一层楼"
print(poem_str)

# 1.拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 2.合并字符串
result = " ".join(poem_list)
print(result)