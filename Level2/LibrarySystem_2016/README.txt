src_skeleton/ : how code should start life from its design
    - no implementation details
    - all method docstrings fully explain the interface of each class

src/ : full working solution for library system.
    - there are some aspects which could be better
    - use cases described in the exercise are implemented
    - there are 2 different implementations for the lists -
        item-list is the better since it uses inheritance
        rather than composition to provide storage functionality.

tests/ : a selection of tests (by no means complete)
    - all use the nosetest framework
    - some use of the class design for tests