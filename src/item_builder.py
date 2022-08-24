
class ItemBuilder:

    library = None
    file_path = ""
    file_data = None

    def __init__(self, library):
        self.library = library

    def load_file(self, f_path):
        """
        Loads, stores and returns the contents of file path given
        :param f_path:
        :return:
        """
        return self.file_data

    def create_item(self, item_data):
        """
        Creates an item (book, DVD, journal..etc) from data given about the item
        :param item_data: A row or dict of information used to create an item
        :return: Populated item object
        """
        return None

