import library


#+
# NAME: Main.py
# PURPOSE: Main (top level) routine for library exercise
# AUTHOR: seg
#-

def startup():
  libcon=LibraryController()

  itemmanager=ItemManager()
  itemmanager.setLibraryController(libcon)
  itemmanager.create_book('Cheese Recipes',0)
  itemmanager.create_book('Beef Recipes',1)

  usermanager=UserManager()
  usermanager.SetLibraryController(libcon)
  usermanager.AddUser()

def main():
  startup()
  exercise1()
