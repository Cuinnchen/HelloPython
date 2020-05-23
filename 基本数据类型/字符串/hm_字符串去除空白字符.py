poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    # 先使用strip方法去除字符串中的空白内容
    # 在使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10,"　"))








def bubble_sort(arr):

    n = len(arr)# n =7
    for j in range(0, n - 1):# 确定循环次数
        for i in range(0, n - 1 - j):# 最大数在第一次循环时已经将其放在最后因故-j
            if arr[i] > arr[i + 1]:# 前后数字对比
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # 满足条件互换位置
                # print(arr)
bubble_sort(arr)
print(arr)
