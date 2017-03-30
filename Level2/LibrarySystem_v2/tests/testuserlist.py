from ..src.user_list import UserList
from ..src.userid_error import UserIdError
from ..src.user import User

import nose.tools as ns


@ns.raises(UserIdError)
def test_find_user():
    new_user = User()
    new_user.set_identification(1)
    ul = UserList()
    ul.add_user(new_user)
    ul._find_user(2)


def test_able_to_borrow():
    new_user = User()
    new_user.set_identification(35)
    user_list = UserList()
    user_list.add_user(new_user)
    result = user_list.able_to_borrow(35, 4, 50)
    ns.assert_true(result)


def test_able_to_borrow_fine_fail():
    new_user = User()
    new_user.set_identification(35)
    new_user._fines = 60.0
    user_list = UserList()
    user_list.add_user(new_user)
    ns.assert_true(user_list.able_to_borrow(35, 4, 50))