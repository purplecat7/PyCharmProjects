from class_code.classAcode import ClassA
import nose.tools as ns
import time

class TestA(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        # ns.assert_true(False, "setup_class run")
        TestA.f = open('test_log.txt', 'w')
        TestA.f.write('setup_class\n')
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # ns.assert_true(False, "teardown_class run")
        time.sleep(1)
        TestA.f.write('teardown_class\n')
        TestA.f.close()


    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        # use self.attribute to keep anything which needs to be accessed later
        self.f = open('test_log.txt', 'a')
        self.f.write('setUp method\n')
        time.sleep(1)


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        self.f = open('test_log.txt', 'a')
        self.f.write('tearDown method\n')
        time.sleep(1)


    def test_init(self):
        self.f = open('test_log.txt', 'a')
        self.f.write('test_init method\n')
        time.sleep(1)
        a = ClassA()
        ns.assert_equal(a.value, "Some Value")
        ns.assert_not_equal(a.value, "Incorrect Value")

    def test_return_true(self):
        self.f = open('test_log.txt', 'a')
        self.f.write('test_return_true method\n')
        time.sleep(1)
        a = ClassA()
        ns.assert_equal(a.return_true(), True)
        ns.assert_not_equal(a.return_true(), False)

    def test_raise_exc(self):
        self.f = open('test_log.txt', 'a')
        self.f.write('test_raise_exc method\n')
        time.sleep(1)
        a = ClassA()
        ns.assert_raises(KeyError, a.raise_exc, "A value")

    @ns.raises(KeyError)
    def test_raise_exc_with_decorator(self):
        self.f = open('test_log.txt', 'a')
        self.f.write('test_raise_exc_with_decorator method\n')
        time.sleep(1)
        a = ClassA()
        a.raise_exc("A message")