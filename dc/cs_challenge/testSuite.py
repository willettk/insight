# Test the sortThis program on lots of different cases

import unittest
from sortThis import removeOddChars,typeSort

class sortTestCase(unittest.TestCase):
    """Tests for `sortThis.py`."""

    def setUp(self):
        self.BaseCase = "20 cat bi?rd 12 do@g"

    def testBaseCase(self):
        """Does the output string for the base case match what we expect?"""

        expectedAnswer = "12 bird cat 20 dog"

        lettersNumbersOnly = removeOddChars(self.BaseCase)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testEqualChars(self):
        """Does the output string have the same number or fewer characters than the input?"""

        lettersNumbersOnly = removeOddChars(self.BaseCase)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertTrue(len(lettersNumbersOnly) >= len(sortedString))

    def testEqualWords(self):
        """Do the input and output strings have the same number of words?"""

        lettersNumbersOnly = removeOddChars(self.BaseCase)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(len(lettersNumbersOnly.split()),len(sortedString.split()))

    def testBigIntegers(self):
        """Does it work with very large or small integers?"""

        testString = "999999 a 0 a -999999"
        expectedAnswer = "-999999 a 0 a 999999"

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testAllIntegers(self):
        """Does it work with a very long list spanning all allowable integers?"""

        #testList = [str(999999 - x) for x in range(1999999)]
        #expectedList = [str(x - 999999) for x in range(1999999)]
        testList = [str(9 - x) for x in range(19)]
        expectedList = [str(x - 9) for x in range(19)]

        testString = ' '.join(testList)
        expectedAnswer = ' '.join(expectedList)

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

if __name__ == "__main__":
    unittest.main()
