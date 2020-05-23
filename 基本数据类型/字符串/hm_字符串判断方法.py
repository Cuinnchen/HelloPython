# 1.判断空白字符

space_str = " \t\n\r"

print(space_str.isspace())

# 2.判断字符串中是否只包含字符串

# num_str = "1.1"
# unicode 字符串
num_str = "\u00b2"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit()) # 判断数字 （1） Unicode字符串
print(num_str.isnumeric()) # 可以判断中文数字