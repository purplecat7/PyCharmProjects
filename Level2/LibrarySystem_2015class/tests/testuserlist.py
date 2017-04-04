__author__ = 'rsmith31'

from src import userList
from src import UserIdError
from src import user

from nose.tools import *


@raises(UserIdError.UserIdError)
def test_find_user():

    new_user = user.User()
    new_user.set_identification(1)

    ul = userList.UserList()
    ul.add_user(new_user)
    ul.find_user(2)