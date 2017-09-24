import unittest
from .challenge import get_array_and_number, get_max, get_num, get_output, get_array


# Unit tests for twig code
class TestArray(unittest.TestCase):

    def test_length(self):
        print("test length")
        false_result1 = get_array_and_number(0, 2)
        false_result2 = get_array_and_number(2, 0)
        true_result1 = get_array_and_number(5, 3)

        self.assertFalse(false_result1)
        self.assertFalse(false_result2)
        self.assertTrue(true_result1)

    def test_get_array(self):
        print("test get array")
        test = get_array(5)
        self.assertEqual(test, [1, 2, 3, 4, 5])
        self.assertNotEqual(test, [1, 2, 3, 4, 5, 6])

    def test_get_num(self):
        print("test get num")
        test1 = get_num(5, 3)
        test2 = get_num(10, 1)
        self.assertEqual(test1, 2)
        self.assertEqual(test2, 10)
        self.assertNotEqual(test1, 3)
        self.assertNotEqual(test2, 3)

    def test_get_max(self):
        print("test get max")
        test1 = get_max(5, 3)
        self.assertEqual(test1, 10)
        self.assertNotEqual(test1, 2)

    def test_get_output(self):
        print("test output")
        num = get_num(5, 3)
        array = get_array(5)
        max = get_max(num, 3)
        test1 = get_output(max, num, array)
        self.assertEqual(test1, [[1, 2], [3, 4], [5]])
