
def crerat_num(all_num):
    print('----1----')
    a, b = 0, 1
    crerat_num = 0
    while crerat_num < all_num:
        print('----2----')
        # yield a # 如果一个函数中有yieid语句，那么这个就不再是函数而是一个生成器模板
        a,b = b, a + b
        crerat_num += 1
        yield a # 如果一个函数中有yieid语句，那么这个就不再是函数而是一个生成器模板
        print('---3---')

a = crerat_num(10)

# for num in a:
#     print(num)
print(next(a))
print(next(a))
print(next(a))