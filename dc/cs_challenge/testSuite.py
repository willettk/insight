# Test the sortThis program on lots of different cases

import unittest
from sortThis import readFile,removeOddChars,typeSort

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

    def testNegativeIntegers(self):
        """Does it work with both positive and negative integers?"""

        testList = [str(9 - x) for x in range(19)]
        expectedList = [str(x - 9) for x in range(19)]

        testString = ' '.join(testList)
        expectedAnswer = ' '.join(expectedList)

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def _testAllIntegers(self):
        """Does it work with a very long list spanning all allowable integers?"""

        testList = [str(999999 - x) for x in range(1999999)]
        expectedList = [str(x - 999999) for x in range(1999999)]

        testString = ' '.join(testList)
        expectedAnswer = ' '.join(expectedList)

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testAllSameInteger(self):
        """Does it work with a list that is just many copies of the same integer?"""

        testList = ["51"]*10
        expectedList = testList

        testString = ' '.join(testList)
        expectedAnswer = ' '.join(expectedList)

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testAllSameWord(self):
        """Does it work with a list that is just many copies of the same word?"""

        testList = ["zrak"]*10
        expectedList = testList

        testString = ' '.join(testList)
        expectedAnswer = ' '.join(expectedList)

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testSymbolWord(self):
        """Does it exit gracefully if it runs into a word that is only symbols?"""

        testString = self.BaseCase + ' $!#'

        self.assertRaises(Exception,removeOddChars(testString))

    def testEmptyLine(self):
        """Does it exit gracefully if it runs into a word that is only symbols?"""

        testString = ""
        expectedAnswer = ""

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testLoisPathological(self):
        """Does it handle legal words/numbers embedded in multiple repeating symbols?"""

        testString = "####-1$$$ -1 -1"
        expectedAnswer = "-1 -1 -1"

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testMinusInWord(self):
        """Does it handle a minus sign embedded within a word?"""

        testString = "1 cat 3 dog 2 aardvark ze-bra"
        self.assertRaises(Exception,removeOddChars(testString))

    def testMinusInNumber(self):
        """Does it handle a minus sign embedded within a number?"""

        testString = "1 cat 3 dog 2 aardvark 50-3"
        self.assertRaises(Exception,removeOddChars(testString))
    
    def testMultipleMinusSignsNumber(self):
        """Does it handle multiple minus signs at the beginning of a number?"""

        testString = "tea coffee 1 0 ----1"
        expectedAnswer = "coffee tea -1 0 1"

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testMultipleMinusSignsLetter(self):
        """Does it handle multiple minus signs at the beginning of a word?"""

        testString = "tea coffee 1 0 ----z-"
        expectedAnswer = "coffee tea 0 1 z"

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

    def testMinusSignsAfter(self):
        """Does it handle minus signs at the beginning and after a number?"""

        testString = "tea coffee 1 0 --1-"
        expectedAnswer = "coffee tea -1 0 1"

        lettersNumbersOnly = removeOddChars(testString)
        sortedString = typeSort(lettersNumbersOnly)
        self.assertEqual(sortedString,expectedAnswer)

if __name__ == "__main__":
    unittest.main()
