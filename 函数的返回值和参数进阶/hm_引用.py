def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num,id(num)))

    # 1.定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    return result
a = 10

print("a变量保存数据的内存地址是 %d" % id(a))

# 注意如果函数有返回值，但是没有定义变量接收
#程序不会报错，但是无法获得返回结果

r = test(a)
print("%s 的内存地址是 %d" %(r,id(r)))



