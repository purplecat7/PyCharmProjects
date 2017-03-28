from library import LibraryController
from ItemManager import ItemManager
from ListManager import ListManager

if __name__ == "__main__":
    """
    This is main. More to follow.
    """
    libraryController = LibraryController()
    # item manager
    # will call the item manager and give it a text file.
    itemManager = ItemManager()
    listManager = ListManager()

    itemManager.setLibraryController(libraryController)
    # will give txt file to item manager
    itemManager.createDatabase('top100.txt')

    # user managerr