
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

a = crerat_num(2)

# for num in a:
#     print(num)
while True:
    try:
        ret = next(a)
        print(ret)
    except Exception as e:
        print(e)
        break
