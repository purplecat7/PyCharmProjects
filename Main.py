import library
import ItemManager
import UserManager

# +
# NAME: Main.py
# PURPOSE: Main (top level) routine for library exercise
# AUTHOR: seg
#-

class numbID:
   idnumber = 0

   def __init__(self):
      pass

   def newID(self):
      numbID.idnumber += 1
      return numbID.idnumber 


def librarycatalogue(libcon,infile):

    idnumb = numbID()
    itemmanager = ItemManager.ItemManager()
    itemmanager.set_library_controller(libcon)
    file=open(infile,'r')
    for line in file:
      itemmanager.create_book(line.strip(), idnumb.newID())
    print 'Number of books added: ',idnumb.idnumber

def librarymembers(libcon):

    idnumb = numbID()
    usermanager = UserManager.UserManager()
    usermanager.SetLibraryController(libcon)
    usermanager.CreateUser(idnumb.newID())
    print 'User ID created: ',idnumb.idnumber
    usermanager.CreateUser(idnumb.newID())
    print 'User ID created: ',idnumb.idnumber

def exercise1(userid, title, libcon):
    libcon.user_checkout(userid, title)

def main():
    print "Initialising library controller..."
    libcon = library.LibraryController()
    print "Populating library catalogue..."
    infile='top100t.txt'
    try:
        librarycatalogue(libcon,infile)
    except:
        print "Catalogue populating failed"
        raise
    print "Populating library members..."
    try:
        librarymembers(libcon)
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
