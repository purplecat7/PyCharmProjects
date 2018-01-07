from class_code.classAcode import ClassA
import nose.tools as ns


class TestA(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        # ns.assert_true(False, "setup_class run")
        pass

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # ns.assert_true(False, "teardown_class run")
        pass

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        # use self.attribute to keep anything which needs to be accessed later
        pass

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        pass

    def test_init(self):
        a = ClassA()
        ns.assert_equal(a.value, "Some Value")
        ns.assert_not_equal(a.value, "Incorrect Value")

    def test_return_true(self):
        a = ClassA()
        ns.assert_equal(a.return_true(), True)
        ns.assert_not_equal(a.return_true(), False)

    def test_raise_exc(self):
        a = ClassA()
        ns.assert_raises(KeyError, a.raise_exc, "A value")

    @ns.raises(KeyError)
    def test_raise_exc_with_decorator(self):
        a = ClassA()
        a.raise_exc("A message")