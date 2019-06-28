import unittest
from world import asia



class TestWorldFunc(unittest.TestCase):
    def test_add(self):
        print('test_add')
        self.assertEqual(3,asia.add(1,2))
        self.assertEqual(3,asia.add(2,1))

    def test_minus(self):
        print('test_minus')
        self.assertEqual(1,asia.minus(3,2))

    def test_mutli(self):
        print('test_multi')
        self.assertEqual(4,asia.multi(2,2))

    def test_divide(self):
        print('test_divide')
        self.assertEqual(2,asia.divide(6,3))
        self.assertEqual(2.5,asia.divide(5,2))

    def setUp(self):
        print('do something before test')

    def tearDown(self):
        print('do something after test')

    @classmethod
    def setUpClass(cls):
        print('this setup only called once')

    @classmethod
    def tearDownClass(cls):
        print('this teardown only called once')

if __name__ == '__main__':
    unittest.main()
