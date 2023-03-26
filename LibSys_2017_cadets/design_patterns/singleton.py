# Singleton/SingletonPattern.py
#  http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
# Also see this for arguments on pros and cons of the pattern:
#   http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class OnlyOne:

    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val


    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
# these prints show that each of
# x, y and z point to the same object
# i.e. each continas the same address
print(z)
print(x)
print(y)
# however the addresses of x, y & z
# are themselves different
print(`x`)
print(`y`)
print(`z`)