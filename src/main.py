from library import LibraryController
from ItemManager import ItemManager
from UserManager import UserManager

if __name__ == "__main__":
    """
    This is main. More to follow.
    """
    # here we call the library controller class.
    libraryController = LibraryController()
    itemManager = ItemManager()
    userManager = UserManager()

    itemManager.setLibraryController(libraryController)
    # initiating the item database.
    itemManager.createDatabase('top100.txt')

    # initiate the user database

    # Johnny Codewarrior
    libraryController.user_checkout(self,user_id,item_title)
