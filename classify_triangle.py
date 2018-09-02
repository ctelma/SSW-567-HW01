'''
I pledge my honor that I have abided by the Stevens Honor System.
Followed the partial solution provided on Canvas to create this.
09/01/2018
Caroline Telma
'''

import unittest     # import Python unittest
import math


def classify_triangle(a,b,c):

    name = ''

    if a == b and b == c and a == c:
        name = 'Equilateral'

    # This is where a fault lies, an improper check for isosceles; A proper check would be: if a==b or a==c or b==c
    elif a == c and b == c:
        name = 'Isosceles'
    # Since the above isosceles check is incorrect, this can also become faulty
    else:
        name = 'Scalene'

    if (a**2 + b**2) == round(c**2, 1):
        name = name + " and Right"

    if (a+b) <= c or (a+c) <= b or (b+c) <= a:
        name = 'Not a triangle'

    return name

class TestTriangles(unittest.TestCase):
    def testIsosceles(self):
        self.assertEqual(classify_triangle(10,9,10), 'Isosceles', 'Should be isosceles')
        self.assertEqual(classify_triangle(4,4,3), 'Isosceles', 'Should be isosceles')
        self.assertEqual(classify_triangle(6,6,7), 'Isosceles', 'Should be isosceles')
        self.assertEqual(classify_triangle(1.0,1.0,math.sqrt(2)), 'Isosceles and Right', 'Should be isosceles and right')

    def testEquilateral(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral', 'Should be equilateral')
        self.assertEqual(classify_triangle(2,2,2),'Equilateral', 'Should be equilateral')
        self.assertEqual(classify_triangle(3,3,3),'Equilateral', 'Should be equilateral')
        self.assertNotEqual(classify_triangle(1,2,3), 'Equilateral', 'Should not be equilateral')


    def testScalene(self):
        self.assertEqual(classify_triangle(2,7,6), 'Scalene', 'Should be scalene')
        self.assertEqual(classify_triangle(5,6,8), 'Scalene', 'Should be scalene')
        self.assertEqual(classify_triangle(4,2,5), 'Scalene', 'Should be scalene')
        self.assertNotEqual(classify_triangle(1,1,1), 'Scalene', 'Should not be scalene')
        self.assertEqual(classify_triangle(3,4,5),'Scalene and Right', 'Should be scalene and right')
        self.assertEqual(classify_triangle(5,12,13),'Scalene and Right', 'Should be scalene and right')
        self.assertEqual(classify_triangle(8,15,17),'Scalene and Right', 'Should be scalene and right')

    def testTriangle(self):
        self.assertEqual(classify_triangle(1,2,1), 'Not a triangle', 'Should not be a triangle')
        self.assertEqual(classify_triangle(3,3,7), 'Not a triangle', 'Should not be a triangle')
        self.assertEqual(classify_triangle(10,10,20), 'Not a triangle', 'Should not be a triangle')
        self.assertNotEqual(classify_triangle(5,5,5), 'Not a triangle', 'Should be a triangle')



if __name__ == '__main__':
    # examples of running the code
    print("Example of running the code:")
    print(classify_triangle(5,5,2))
    print(classify_triangle(0,2,1))
    print(classify_triangle(1.0,1.0,math.sqrt(2)))

    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
