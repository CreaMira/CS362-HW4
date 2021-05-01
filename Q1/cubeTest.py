import unittest
import cube

class testCase(unittest.TestCase):
    def test_cube_base(self):
        self.assertEqual(cube.cube(1,1,1), 1)
        self.assertEqual(cube.cube(4,3,2), 24)
    
    def test_cube_negative(self):
        with self.assertRaises(ValueError):
            cube.cube(-1, 2, 3)
            cube.cube(4, -1, 5)
            cube.cube(6, 7, -1)
            
    def test_cube_string(self):
        with self.assertRaises(ValueError):
            cube.cube("this","is","string")


if __name__ == '__main__':
    unittest.main()