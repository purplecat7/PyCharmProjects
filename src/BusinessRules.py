"""
Business rules e.g. is user eligible to borrow from library?
"""

from .User import User

MAX_LOANS = 5
MAX_FINES = 50  # £


def check_max_loans(user: User) -> bool:
    """
    user currently has fewer than MAX_LOANS
    :returns: user passes check and is eligible to borrow from library
    """
    return user.get_number_loans() <= MAX_LOANS


def check_max_fines(user: User) -> bool:
    """
    user currently has less than MAX_FINES
    :returns: user passes check and is eligible to borrow from library
    """
    return user.get_fines() <= MAX_FINES


USER_ELIGABLE_TO_BORROW = (
    check_max_loans,
    check_max_fines
)
