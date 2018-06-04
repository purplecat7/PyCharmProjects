"""
Class for user for library example

"""

class User():

	"""
	User class for creating and managing user of library

	"""

	def __init__(self):
		"""
		Initialise a user with ID number and initial fine which will be 0
		"""
		# attributes of a user are:
		# id, current fines
		# have to generate ID's, incrementing numbers
		# current fines start at 0
		# fines could be a dict for each item?
		pass

	def __del__(self):
		"""
		Clean up the user if they leave library

		:return:
		"""

		# user may be removed to this method will remove that user?
		pass

	def able_to_borrow(self):
		"""
		Check whether a user is able to borrow an item

		:return: boolean
		"""
		pass

	def checkout(self, item):
		"""
		Checkout an item. Calls to libraries item list

		:param item: item object that is to be checked out
		:return:
		"""
		pass

	def return_item(self, item):
		"""
		Return item back to library for current user

		:return:
		"""
		pass