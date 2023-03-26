__author__ = 'nerc'
from LibSys_2017_cadets.src.user import User
from LibSys_2017_cadets.src.userlist import UserList
import LibSys_2017_cadets.src.library_exceptions as lex
import nose.tools as ns


def test_able_to_borrow():
    ghost_user = User(35)
    user_list = UserList()
    user_list.add_user(ghost_user)
    result = user_list.able_to_borrow(35, 4, 50)
    ns.assert_true(result)

@ns.raises(lex.FineHighError)
def test_able_to_borrow_fine_fail():
    ghost_user = User(35)
    ghost_user._fines = 60.0
    user_list = UserList()
    user_list.add_user(ghost_user)
    result = user_list.able_to_borrow(35, 4, 50)
