
def crerat_num(all_num):
    print('----1----')
    a, b = 0, 1
    crerat_num = 0
    while crerat_num < all_num:
        ret = yield a
        print('>>>>ret',ret)
        a,b = b, a + b
        crerat_num += 1


a = crerat_num(2)

ret = next(a)
print(ret)

ret = a.send('111')
print(ret)
print(ret)
# for num in a:
#     print(num)
