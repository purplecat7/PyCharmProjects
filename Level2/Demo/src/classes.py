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

def main():
    new_iceland = make_iceland()
    print (new_iceland.name)
    my_car = Car('W100 EVO', 'blue')
    print (my_car.reg)






class MyClass:
    #class attributes
    myDict = {"key1": 10, "key2": False }
    
    #this method called whenever new instance created
    def __init__(self):
        #initialise attributes
        self.privateAttribute = None
        self.privateList = list()
        
    #this method called whenever object destroyed
    def __del__(self):
        pass
    
    #public methods
    def doSomething(self, parameter):
        self.privateList = parameter
        self.__doHelperJob(parameter)
        
    #private methods        
    def __doHelperJob(self, another_parameter):
        self.privateAttribute = another_parameter * MyClass.myDict["key1"]
        

        
        
class Bar:
    def __init__(self):
        self.biz = "boo!"
class Foo(Bar):
    def __init__(self):
        super(Foo, self).__init__()
        self.baz = 5
        
        
if __name__ == "__main__":
    main()


        
        
