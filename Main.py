import library
import ItemManager
import UserManager

# +
# NAME: Main.py
# PURPOSE: Main (top level) routine for library exercise
# AUTHOR: seg
#-

class NumbID:
   idnumber = 0

   def __init__(self):
      pass

   def new_id(self):
      NumbID.idnumber += 1
      return NumbID.idnumber 


def library_catalogue(libcon,infile):

    idnumb = NumbID()
    itemmanager = ItemManager.ItemManager()
    itemmanager.set_library_controller(libcon)
    file=open(infile,'r')
    for line in file:
      itemmanager.create_book(line.strip(), idnumb.new_id())
    print 'Number of books added: ',idnumb.idnumber

def library_members(libcon):

    idnumb = NumbID()
    usermanager = UserManager.UserManager()
    usermanager.SetLibraryController(libcon)
    usermanager.CreateUser(idnumb.new_id())
    print 'User ID created: ',idnumb.idnumber
    usermanager.CreateUser(idnumb.new_id())
    print 'User ID created: ',idnumb.idnumber

def exercise1(userid, title, libcon):
    libcon.user_checkout(userid, title)

def exercise2(userid, title, libcon):

    fine = libcon.add_item(userid,libcon)
    print "User: ",userid
    print "Total Fine: ",fine

def main():
    print "Initialising library controller..."
    libcon = library.LibraryController()
    print "Populating library catalogue..."
    infile='top100t.txt'
    try:
        library_catalogue(libcon,infile)
    except:
        print "Catalogue populating failed"
        raise
    print "Populating library members..."
    try:
        library_members(libcon)
    except:
        print "Catalogue populating failed"
        raise
    print "Exercise 1..."
    try:
        exercise1(100, 'The Kite Runner', libcon)
    except:
        print "Exercise 1 failed"
        raise

if __name__ == '__main__':
   main()
