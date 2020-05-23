name_list = ["zhangsan", "lisi", "wangwu"]

# 1 、取值和取索引
print(name_list[2])
# list index out of range -列表索引超出范围

# 知道数据的内容，想确定数据在列表中的位置
print(name_list.index("lisi"))
# 使用index方法需注意，如果传递的数据不在列表中，程序会报错

# 2 、修改
name_list[1] = "李四"
# name_list[3] = "王小二"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错
print(name_list)

# 3 、增加
# append 方法可以向列表末尾增加元素
name_list.append("王小二")
# insert可以再列表的指定位置插入数据
name_list.insert(1, "小美眉")

# extend 方法可以把其他列表的完整内容增加到当前列表
temp_list = ["孙悟空","猪二哥"]
name_list.extend(temp_list)

# 4 、删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")


# pop方法默认可以把列表中最后一个元素
name_list.pop()

# pop方法可以指定要删除元素的索引
name_list.pop(3)

# clear 方法可以清空列表
name_list.clear()

print((name_list))



# （知道）使用del关键字删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字本质上用来将一个变量从内存中删除的
# 注意：如果使用del 关键字将变量从内存中删除
# 后续代码就不能再使用这个变量了