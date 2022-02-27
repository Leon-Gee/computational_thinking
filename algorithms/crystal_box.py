import unittest

def is_legal_age(age):
    return age >= 18


class crystal_box_test(unittest.TestCase):
    
    def test_is_legal_age(self):
        age = 20

        result = is_legal_age(age)

        self.assertEqual(result, True)
    

    def test_is_not_legal_age(self):
        age = 15

        result = is_legal_age(age)

        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
