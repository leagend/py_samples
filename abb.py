import time

class abb:
    def __init__(self):
        self.value = 1

    def set_value(self, value0):
        self.value =  value0

    def get_value(self):
        return self.value

    def timeit( func):
        def wrapper(*args):
            # self.set_value
            instance = args[0]
            print instance
            instance.set_value(2)
            start = time.clock()
            if args[-1] == True:
                print args,'rob'
            func(*args)
            end =time.clock()
            print 'used:', end - start
        return wrapper

    @timeit
    def foo(self, a, b = False):
        print 'in foo()',a, self.get_value()

    @timeit
    def foo2(self):
        print 'in foo()'

ins = abb()
print ins
ins.foo('hello', True)
print
ins.foo('hi')
print
ins.foo2()


