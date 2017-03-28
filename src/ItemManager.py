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
        for ind_title, title in enumerate(len(title_list)):
            if ind_title <30:
                book_instance = Book(title, 'Book_%3i'%(ind_title))
                LibraryController.add_item(book_instance)
            elif ind_title >=30 && ind_title < 60:
                DVD_instance = DVD(title, 'DVD_%3i'%(ind_title))
                LibraryController.add_item(DVD_instance)
            elif ind_title >=60 && ind_title < len(title_list):
                Journal_instance = Journal(title, 'Journal_%3i'%(ind_title))
                LibraryController.add_item(Journal_instance)

    def createItem(self, title, itemType):
        pass
    def createBook(self, title):
        pass
    def createDVD(self,title):
        pass
    def createJournal(self, title):
        pass
    def set_library_controller(self, libraryController):
        self._libraryController = libraryController
