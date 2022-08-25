
class CheckoutError(Exception):

    def __init__(self):
        self.message = "Checkout error. Please check max loans and max fines."

    def __str__(self):
        return repr(self.message)