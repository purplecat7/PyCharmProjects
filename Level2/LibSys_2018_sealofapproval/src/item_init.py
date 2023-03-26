import item

class ItemInit():
    """Adds stuff."""
    
    def __init__(self):
        self.lib_mgr = None
        
    def set_library_manager(self, library):
        """sets library manager"""
        self.lib_mgr = library

    def create_book(self, name, id):
        """Adds a book to item list."""
        theitem = item.Book(id, name)
        self.lib_mgr.add_item(theitem)
        
    def create_dvd(self, name, id):
        """Adds a dvd to item list."""
        theitem = item.Dvd(id, name)
        self.lib_mgr.add_item(theitem)
    
    def create_journal(self, name, id):
        """Adds a journal to item list."""
        theitem = item.Journal(id, name)
        self.lib_mgr.add_item(theitem)
        