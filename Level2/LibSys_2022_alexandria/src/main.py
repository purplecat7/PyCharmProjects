from Level2.LibSys_2022_alexandria.src.library import Library
from Level2.LibSys_2022_alexandria.src.item_builder import ItemBuilder
from Level2.LibSys_2022_alexandria.src.user_builder import UserBuilder
from datetime import datetime, timedelta


def scenario_jonny_codewarrior(library):
    # 0 = Jonny
    # One outstanding book, not overdue
    library.checkout_item(1, "Angels and Demons", date=datetime.now() - timedelta(days=1))
    # Check out book, "Document, Your Job depends on it"
    if library.can_checkout(1):
        library.checkout_item(1, "Document, Your job depends on it")
    else:
        print("Unable to check out item... :(")
    print('HUZZAH!!!')

def scenario_judy_hacker(library):
    """
    Judy Hacker, has fines of £2 outstanding,
    would like a DVD “Debugging to music”,
    does have a book out (not overdue) and is bringing back an overdue journal.
    """
    library.checkout_item(2, "New Moon", date=datetime.now() - timedelta(days=32))
    library.return_item(2, "New Moon")
    library.checkout_item(2, "Twilight")
    library.checkout_item(2, "Debugging to music")
    library.return_item(2, "Pirates of the Caribbean: The Journal")


def scenario_miss_marple(library):
    # 2 = Miss
    library.checkout_item(1, "Sleuthing in C#", date=datetime.now() - timedelta(days=8271))  # C# first appeared in 2000
    # Miss marple tries to check out journal 'Sleuthing in C#'
    if library.check_user_can_checkout(2):
        library.checkout_item(3, "Sleuthing in C#")
    else:
        print("Unable to check out item... :(")


def scenario_eric_halfbee(library):
    """
    Eric Halfbee comes in with a pile of overdue items,
    but doesn’t know if he has enough money to pay off his debts.
    If he has, he’d like a borrow a DVD.
    """
    library.checkout_item(4, "Life of Pi", date=datetime.now() - timedelta(days=40))
    library.checkout_item(4, "Labyrinth", date=datetime.now() - timedelta(days=40))
    library.checkout_item(4, "The Tales of Beedle the Bard", date=datetime.now() - timedelta(days=40))
    library.return_item(4, "Life of Pi")
    library.return_item(4, "Labyrinth")
    library.return_item(4, "The Tales of Beedle the Bard")
    fine = library.get_total_fine(4)
    print(f"Outstanding fine: £{fine:.2f}")
    library.pay_fine(4, 10)
    library.checkout_item(4, "Pirates of the Caribbean")


def build_library(library):
    item_builder = ItemBuilder()

    item_builder.set_library(library)

    item_builder.load_books_in_file("top100t.txt")
    item_builder.create_dvd("Pirates of the Caribbean")
    item_builder.create_journal("Pirates of the Caribbean: The Journal")
    item_builder.create_journal("Sleuthing in C#")

    item_builder.populate_library()


def build_users(library):
    user_builder = UserBuilder()
    user_builder.set_library(library)

    # TODO: Generate users from Enums instead of for loop
    for i in range(0, 4):
        user_builder.create_user()


if __name__ == '__main__':
    print("Welcome to Alexandria")

    lib_controller = Library(max_loans=5, max_fines=50)

    build_library(lib_controller)

    build_users(lib_controller)

    # Run scenario's
    scenario_jonny_codewarrior(lib_controller)
    scenario_judy_hacker(lib_controller)
    scenario_miss_marple(lib_controller)
    scenario_eric_halfbee(lib_controller)
