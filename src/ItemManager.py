from itemSubclasses import Book
from itemSubclasses import DVD
from itemSubclasses import Journal
from library import LibraryController

class ItemManager:

    def __init__(self):
        pass
    def __del__(self):
        pass

    def _extract_titles(self,textfile):
        # Open the text files and extract titles
        f             = open(textfile)
        list_of_titles = []
        for i in range(0,99):
            list_of_titles.append(f.next().strip())
        f.close()
        return list_of_titles

    def create_database(self,textfile):
        # Open the text files and extract titles
        title_list = self._extract_titles(textfile)
        for ind_title, title in enumerate(len(title_list)):
            if ind_title <30:
                book_instance = Book(title, ind_title)
                self._libraryController.add_item(book_instance)
            elif ind_title >=30 and ind_title < 60:
                DVD_instance = DVD(title, ind_title)
                self._libraryController.add_item(DVD_instance)
            elif ind_title >=60 and ind_title < len(title_list):
                Journal_instance = Journal(title, ind_title)
                self._libraryController.add_item(Journal_instance)

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
