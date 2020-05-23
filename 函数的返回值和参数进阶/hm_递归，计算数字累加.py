def sum_numbers(num):
    # 1.出口
    if num ==1:
        return 1
    return num  + sum_numbers(num - 1)
    # 2.数字的累加 num + （1...num -1)
    # 假设sum_numbers 能够正确的处理 1...num -1
    # temp = sum_numbers(num-1)
    # # 两个数字的相加
    # return num + temp

result = sum_numbers(3)
print(result)
