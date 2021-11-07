def set_fun_1(fun):
    def call_fun():
        return  '<h1>' + fun() + "</h1>"
    return call_fun

def set_fun_2(fun):
    def call_fun():
        return  '<td>' + fun() + "</td>"
    return call_fun


@set_fun_1
@set_fun_2
def get_str():
    return 'haha'


print(get_str())