# -*- coding: utf-8 -*-

class MyError(Exception):
    def __init__(self, val):
        print ('init MyError')
        self.value = val
        
    def __str__(self):
        #repr() returns a string representation of the object
        return repr(self.value)

        
class MySpecificError(MyError):
    def __init__(self, val, info):
        print ('init MySpecificError')
        self.value = val
        self.message = info
        
    def __str__(self):
        print ('str')
        print super(MySpecificError, self).__str__()
        return repr(self.message)


def aFunction(fileArg):
    try:
        age = 21
        name = "jane"
        myFile = open(fileArg, 'r')
    except IOError:
        print("IOERROR, cannot open ", fileArg)
    except TypeError as te:
        print(te.message)
        raise te
    except:
        raise TypeError
    else:
        #code to be executed after try
        #but any exceptions not caught here
        myFile.close()        


def main():
    try:
        print('boo!')
        raise MyError(1)
    except MyError as e:
        print(e.value)
        
    try:
        print('boo!!')
        raise MySpecificError(2, "ouch")     
    except MySpecificError as e:
        print (e)
        print (e.message)


if __name__ == '__main__':
    main()
