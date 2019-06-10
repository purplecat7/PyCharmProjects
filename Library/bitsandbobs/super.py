class mylist(list):
    def __init__(self):
        pass
    def mylen(self):
        print(len(self))
    def myadd(self, item):
        print('adding ' + str(item))
        self.append(item)
    def mysuperadd(self, item):
        print('adding super ' + str(item))
        super(mylist, self).append(item)

asd = mylist()
asd.myadd(1)
asd.mysuperadd(2)
asd.mylen()
asd.append(3)
asd.mylen()
