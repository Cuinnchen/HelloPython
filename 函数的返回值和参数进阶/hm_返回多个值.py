def measure():
    print("测量开始。。。")
    temp = 39
    wetness = 50
    print("测量结束。。。")

    # 元祖-可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 如果函数返回的类型是元祖，小括号可以省略
    return  temp,wetness

# 元祖=result
result = measure()
print(result)

# 需要单独的处理温度或者湿度

print("温度是：",result[0])


# 如果函数返回的类型是元祖，同时希望单独的处理元祖中的元素
# 可以使用多个变量，一次接受函数的返回结果
# 注意，使用多个变量接受结果时，变量的个数应该和元祖中元素的个数保持一致
gl_temp,gl_wetness = measure()

print(gl_temp)
print(gl_wetness)



a = 5
b = 100

a = a + b
b = a - b
a = a -b
# a,b = b,a
print(a,b)