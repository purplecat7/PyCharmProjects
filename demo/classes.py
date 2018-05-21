# -*- coding: utf-8 -*-


class Countries():
    def __init__(self):
        self.name = None
        self.popln = 0
        self.likeCarrots = False

def make_iceland():
    iceland = Countries()
    iceland.name = 'Iceland'
    iceland.popln = 300000
    iceland.likeCarrots = True
    return iceland

class Car():
    def __init__(self, the_reg, the_colour):
        self.reg = the_reg
        self.colour = the_colour


class MyClass:
    # class attributes
    myDict = {"key1": 10, "key2": False }
    
    # this method called whenever new instance created
    def __init__(self):
        # initialise instance attributes
        self.__privateAttribute = 0
        self.__privateList = list()
        
    # this method called whenever object destroyed
    def __del__(self):
        self.__privateList = None
    
    # public methods - anyone can see these
    def do_something(self, a_list):
        self.__privateAttribute = len(a_list)
        self.__do_secret_helper_job(a_list)
        self._do_hidden_helper_job()

    # 'protected' methods - you shouldn't use them but you can see them
    def _do_hidden_helper_job(self):
        self.__privateAttribute += 1

    # private methods - these get mangled to try to hide them
    def __do_secret_helper_job(self, the_list):
        self.__privateList.append(the_list[0] * MyClass.myDict["key1"])

    @staticmethod
    def add_numbers(x, y):
        return x + y

    @classmethod
    def get_dict(cls):
        return cls.myDict


class Bar:
    def __init__(self):
        self.biz = "boo!"
class Foo(Bar):
    def __init__(self):
        super(Foo, self).__init__()  # Python2
        # super().__init__()   # Python3
        self.baz = 5


def main():
    new_iceland = make_iceland()
    print (new_iceland.name)
    my_car = Car('W100 EVO', 'blue')
    print (my_car.reg)
    print (MyClass.myDict)
    myclass = MyClass()
    myclass.do_something((1,2,3))
    myclass._do_hidden_helper_job()

        
if __name__ == "__main__":
    main()


        
        
