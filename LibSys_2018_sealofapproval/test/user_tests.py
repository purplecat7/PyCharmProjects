from LibSys_2018_sealofapproval.src.user import User
import nose.tools as ns


class TestUser():
	"""
	Test class for testing user methods

	"""

	def test_init(self):
		"""
		Test init of user

		:return:
		"""
		self.user = User(999)

	#def test_able_to_borrow(self):
	#	"""
	#	Test able to borrow for user

	#	:return:
	#	"""
	#	maxfines = 5
	#	maxallowed = 4
	#	self.user.able_to_borrow(maxfines, maxallowed)


