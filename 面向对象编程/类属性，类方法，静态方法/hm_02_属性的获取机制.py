class Tool(object):
    count = 0
    def __init__(self,name):

        self.name = name

        # 让类属性的值+1
        Tool.count += 1

# 1.创建工具对象

tool1 = Tool("斧头")
tool2 = Tool("锄头")
tool3 = Tool("镰刀")

# print(Tool.count)

print("工具对象总数 %d" % tool1.count)

