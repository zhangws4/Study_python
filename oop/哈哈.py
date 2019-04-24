# 三种方法的案例
class Person:
    def eat(self):
        print(self)
        print("Eating....")

    # 类方法
    # 类方法的第一个参数，一般命名为 cls,区别于 self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.............")

    # 静态方法
    # 不需要用第一个参数或自身
    @staticmethod
    def say():
        print("Saying........")


yueyue = Person()
#实例方法
yueyue.eat()
#类方法
Person.play()