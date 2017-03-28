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

    # code to add user.
    # first need to ask, are you a user
    user_present = input('Are you a new user (yes/no) ? ')
    if user_present =='yes':
        user_ID_choice = input('Please choose an ID name? ')
        libraryController.add_user(user_ID_choice)
        print 'thank you ' + user_ID_choice +'. You are now a library user.'
    else user_present == 'no':
        user_ID_choice = input('Please tell us your user ID name? ')
        print ('What would you like to do out of these options? ')
        operation_choice = input('1) Take out book, 2) Return book, 3) Pay Fine, 4) Check whether a book is on loan? '+\
                                 '5) Check how much you owe due to fines?')

        if operation_choice== 1:
            # code to checkout book
            item_title = input('What is the item title you would like to take out?')
            libraryController.user_checkout(user_ID_choice,item_title)
        elif operation_choice== 2:
            item_title = input('What item would you like to return?')
            libraryController.user_return(user_id,item_title)
        elif operation_choice==3:

            libraryController.pay_fine(user_id,amount)


    # code to find user
    libraryController.user_find(user_id)

    libraryController.add_item(item)

    libraryController.is_on_loan(item_title)