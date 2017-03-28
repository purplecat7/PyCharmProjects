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

    itemManager.set_library_controller(libraryController)
    userManager.set_library_controller(libraryController)
    # initiating the item database.
    itemManager.createDatabase('top100.txt')


    # code to checkout book
    libraryController.user_checkout(user_id,item_title)
    # code to find user
    libraryController.user_find(user_id)
    libraryController.user_return(user_id,item_title)
    libraryController.add_item(item)
    libraryController.add_user(user_id)
    libraryController.pay_fine(user_id,amount)
    libraryController.is_on_loan(item_title)