import unittest

def sum_2_numbers(num_1, num_2):
    return num_1 + num_2

class black_box_test(unittest.TestCase):
    
    #all test must always start with test word
    def test_sum_positive(self):
        num_1 = 10
        num_2 = 5

        result =  sum_2_numbers(num_1, num_2)

        self.assertEqual(result, 15)


    def test_sum_negative(self):
        num_1 = -10
        num_2 = -7

        result = sum_2_numbers(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()


