from itemSubclasses import Book
from itemSubclasses import DVD
from itemSubclasses import Journal
from library import LibraryController

class ItemManager:

    def __init__(self):
        pass
    def __del__(self):
        pass


    def extract_titles(self,textfile):
        """ This function opens a text file, iterates through each line
        each title is then added to a list
        The list is then returned
        Only the first 100 lines are used"""

        # Open the text file
        f             = open(textfile)
        list_of_items = []

        # Loop through each line and append to a list
        for i in range(0,len(textfile)):
            list_of_items.append(f.next().strip())
        f.close()

        return list_of_items

    def create_database(self,textfile):
        """ This function opens a textfile using _extract_titles
        It then loops through the list
        The first 30 are created as books
        the next 30 are created as DVDs
        the last ones are created as Journals
        This function uses the classes Book,DVD and Journal from itemSubclasses
        It also uses add_item from _libraryController"""

        # Open the text files and extract titles
        title_list = self.extract_titles(textfile)

        # Loop through the list of titles
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

    def set_library_controller(self, libraryController):
        self._libraryController = libraryController
