import classes as c

myclass = c.MyClass()
print myclass.do_something((1, 2, 3))
print myclass._do_hidden_helper_job()

class ShannonsClass():
    def __init__(self):
        self.__init__()
        self.library_manager = 'Shannon'
        
    def do_magic(self, n):
        self.name = self.__privateAttribute
        print self.name

s = ShannonsClass()
s.do_magic(9)