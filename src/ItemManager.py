from itemSubclasses import Book
from itemSubclasses import DVD
from itemSubclasses import Journal
from library import LibraryController

class ItemManager:

    def __init__(self):
        pass
    def __del__(self):
        pass

    def extractTitles(self,textfile):
        # Open the text files and extract titles
        f             = open(textfile)
        list_of_items = []
        for i in range(0,99):
            list_of_items.append(f.next().strip())
        f.close()
        return list_of_items

    def createDatabase(self,textfile):
        # Open the text files and extract titles
        title_list = extractTitles(textfile)
        for ind_title, title in enumerate(title_list):
            if ind_title <30:
                book_instance = Book(title, 'Book_%3i'%(ind_title))
                LibraryController.add_item(book_instance)



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
