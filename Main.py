import library
import ItemManager
import UserManager

# +
# NAME: Main.py
# PURPOSE: Main (top level) routine for library exercise
# AUTHOR: seg
#-

def startup():
    # Nomenclature
    #   Item ID from #0
    #   User ID from #1000

    libcon = library.LibraryController()

    itemmanager = ItemManager.ItemManager()
    itemmanager.set_library_controller(libcon)
    itemmanager.create_book('Cheese Recipes', 0)
    itemmanager.create_book('Beef Recipes', 1)

    usermanager = UserManager.UserManager()
    usermanager.SetLibraryController(libcon)
    usermanager.CreateUser(1000)
    usermanager.CreateUser(1001)

    return libcon


def exercise1(userid, title, libcon):
    libcon.user_checkout(userid, title)

def main():
    print "Startup..."
    try:
        libcon = startup()
    except:
        print
        "Startup failed"
        raise
    print "Exercise 1..."
    try:
        exercise1(1000, 'Beef Recipes', libcon)
    except:
        print
        "Exercise 1 failed"
        raise

if __name__ == '__main__':
   main()
