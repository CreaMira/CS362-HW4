import unittest
import fullName

class testCase(unittest.TestCase):
    def test_fullName_base(self):
        fName = "fName"
        lName = "lName"
        self.assertEqual(fullName.nameGenerate(fName, lName), "fName lName")


if __name__ == '__main__':
    unittest.main()