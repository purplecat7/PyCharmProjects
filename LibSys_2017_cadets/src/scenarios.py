from LibSys_2017_cadets.src.library import LibraryController
from LibSys_2017_cadets.src.user import User
import datetime as dt
import ItemManager as bob

lc=LibraryController()
im = bob.ItemManager()
im.set_library_controller(lc)
im.create_database('top100t.txt')

JohnnyCodewarrior = User(666)
lc.add_user(JohnnyCodewarrior)
lc.user_checkout(666,'Twilight', date=dt.datetime(2017, 3, 25))
lc.user_checkout(666, 'Document, Your job depends on it')