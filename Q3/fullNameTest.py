import unittest
import fullName

class testCase(unittest.TestCase):
    def test_fullName_base(self):
        fName_1 = "fName"
        lName_1 = "lName"
        self.assertEqual(fullName.nameGenerate(fName_1, lName_1), "fName lName")

    def test_fullName_Abb(self):
        fName_2 = "F"
        lName_2 = "lName"
        self.assertEqual(fullName.nameGenerate(fName_2, lName_2), "lName, F.")

    def test_fullName_str(self):
        fName_3 = "1234"
        lName_3 = "lName"
        with self.assertRaises(ValueError):
            fullName.nameGenerate(fName_3, lName_3)


if __name__ == '__main__':
    unittest.main()