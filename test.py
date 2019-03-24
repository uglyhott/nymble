import unittest
import Nymble

class NymbleTest(unittest.TestCase):

    def test_input_is_list(self):
        self.assertTrue(Nymble._is_list())


if __name__ == '__main__':
    unittest.main()