from class_code.classAcode import ClassA
import nose.tools as ns
import time

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

class TestA(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        # ns.assert_true(False, "setup_class run")
        print('setup_class\n')

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # ns.assert_true(False, "teardown_class run")
        print('teardown_class\n')


    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        # use self.attribute to keep anything which needs to be accessed later
        print('setUp method\n')


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        print('tearDown method\n')


    def test_init(self):
        print('test_init method\n')
        a = ClassA()
        ns.assert_equal(a.value, "Some Value")
        ns.assert_not_equal(a.value, "Incorrect Value")

    def test_return_true(self):
        print('test_return_true method\n')
        a = ClassA()
        ns.assert_equal(a.return_true(), True)
        ns.assert_not_equal(a.return_true(), False)

    def test_raise_exc(self):
        print('test_raise_exc method\n')
        a = ClassA()
        ns.assert_raises(KeyError, a.raise_exc, "A value")

    @ns.raises(KeyError)
    def test_raise_exc_with_decorator(self):
        print('test_raise_exc_with_decorator method\n')
        a = ClassA()
        a.raise_exc("A message")