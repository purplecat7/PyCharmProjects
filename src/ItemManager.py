from itemSubclasses import Book
from itemSubclasses import DVD
from itemSubclasses import Journal

class ItemManager:

    def __init__(self):
        pass
    def __del__(self):
        pass
    def createItem(self, title, itemType):
        pass
    def createBook(self, title):
        f = open(top100)
        for i in range(0,29):
            title = f.next().strip()
        f.close()
        return title
    def createDVD(self,title):
        f = open(top100)
        for i in range(30,59):
            title = f.next().strip()
        f.close()
        return title
    def createJournal(self, title):
        f = open(top100)
        for i in range(60,99):
            title = f.next().strip()
        f.close()
        return title
    def set_library_controller(self, libraryController):
        self._libraryController = libraryController
