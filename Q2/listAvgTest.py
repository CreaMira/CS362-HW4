import unittest
import listAvg

class testCase(unittest.TestCase):
    def test_listAvg_base(self):
        test_list_1 = [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual(listAvg.avg(test_list_1), 4.5 )
    
    def test_listAvg_digit(self):
        test_list_2 = [1,2,7]
        self.assertEqual(listAvg.avg(test_list_2), 3.33 )
    
    def test_listAvg_enpty(self):
        test_list_3 = []
        with self.assertRaises(ValueError):
            listAvg.avg(test_list_3)


if __name__ == '__main__':
    unittest.main()