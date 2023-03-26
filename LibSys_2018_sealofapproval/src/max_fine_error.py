class MaxFinesError(Exception):
	"""
	Error exception class for maximum fine exceeded

	"""
	def __init__(self, fine):
		"""
		Init max fine class

		:param: fine: the fine that the user  has so we can print a useful message

		"""
		self.fine = fine

	def __str__(self):
		"""
		Return a useful error message if the exception is raised and error is printed out

		:return: useful error message with users current fines in
		"""

		return "You have exceeded your maximum allowed fines. Your current fine is" + str(self.fine) + \
		       ". I'm sending the bailiffs."
