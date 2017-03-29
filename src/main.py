'''
Perform library operations and make new user.

Functions used:
    perform_library_operation(...): Perform a library operation.
    new_user_query(...): Create a new user query.
'''

from library import LibraryController
from ItemManager import ItemManager
from usermanager import UserManager

def perform_library_operation():
    '''
    This function allows  all library operations.
    :return:
    '''
    # find out user ID
    user_ID_choice = raw_input('Please tell us your user ID name? ')
    print ('What would you like to do out of these options? ')
    # find out the operation choice requested. Needs to be an integer between 1 and 6.
    operation_choice = raw_input('1) Take out book, \n'
                                 '2) Return book, \n'
                                 '3) Pay Fine, \n'
                                 '4) Check whether a book is on loan? \n'
                                 '5) Check how much you owe due to fines?\n'
                                    '6) Add a new user?')
    # while loop - take operation raw_input and ask for new number if above 6.
    while operation_choice>6:
            operation_choice = raw_input('You chose unwisely, try again please?')
    if operation_choice== 1:
        # code to checkout book
        item_title = raw_input('What is the item title you would like to take out?')
        libraryController.user_checkout(user_ID_choice,item_title)
    elif operation_choice== 2:
        # code to return item
        item_title = raw_input('What item would you like to return?')
        libraryController.user_return(user_ID_choice,item_title)
    elif operation_choice==3:
        # code to pay fines
        amount = raw_input('How much would you like to pay?')
        libraryController.pay_fine(user_ID_choice,amount)
    elif operation_choice==4:
        # check whether item is present
        item_title = raw_input('What is the item title you would like to check?')
        libraryController.is_on_loan(item_title)
    elif operation_choice==5:
        # check the amount owed by user
        libraryController.get_user_fine(user_ID_choice)
    elif operation_choice==6:
        # add an item.
        item = raw_input('Please input the item title?')
        item_type = raw_input('What type of item is it? (DVD, book, journal)')
        itemManager.createItem(item,item_type)

def new_user_query():
    '''
    Functin to add a new user
    :return:
    '''
    # Allowing own user ID name
    user_ID_choice = raw_input('Please choose an ID name? ')
    libraryController.add_user(user_ID_choice)
    print 'thank you ' + user_ID_choice +'. You are now a library user.'


if __name__ == "__main__":
    '''
    Script to run the manage the library users and their accounts.
    '''
    # here we call the library controller class.
    libraryController = LibraryController()
    itemManager = ItemManager()
    userManager = UserManager()

    # set library controller
    itemManager.set_library_controller(libraryController)
    userManager.set_library_controller(libraryController)
    # initiating the item database.
    itemManager.create_database('top100t.txt')

    # code to add user.
    # first need to ask, are you a user
    user_present = raw_input('Are you a new user (yes/no) ? ')
    if user_present =='yes':
        # will generate a new user
        new_user_query()
    elif user_present == 'no':
        # function to perform operation
        perform_library_operation()