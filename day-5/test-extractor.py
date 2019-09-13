from unittest import TestCase
from io import StringIO

from extractor import SubsequenceExtractor


class TestExtractorParsing(TestCase):
    """
    Tests for the TestExtractor class when we initialize it with some offsets.
    """

    def testNoStartInRange(self):
        """
        If we pass in -500 then ValueError should be raised.
        """
        offsets = StringIO('-500')
        error = r'^Start cannot be negative\.$'
        self.assertRaisesRegex(ValueError, error,
                               SubsequenceExtractor, offsets)

    def testNonNumericOffset(self):
        """
        If we pass in 'hello' then ValueError should be raised.
        """
        offsets = StringIO('hello')
        error = r"^Could not parse line 'hello'!$"
        self.assertRaisesRegex(ValueError, error,
                               SubsequenceExtractor, offsets)

    def testOneNumberOneNonNumericInRange(self):
        """
        If we pass in '3 - hello' then ValueError should be raised.
        """
        offsets = StringIO('3 - hello')
        error = r"^invalid literal for int\(\) with base 10: ' hello'$"
        self.assertRaisesRegex(ValueError, error,
                               SubsequenceExtractor, offsets)

    def testOneNonNumericOneNumberInRange(self):
        """
        If we pass in 'hello - 3' then ValueError should be raised.
        """
        offsets = StringIO('hello - 3')
        error = r"^invalid literal for int\(\) with base 10: 'hello '$"
        self.assertRaisesRegex(ValueError, error,
                               SubsequenceExtractor, offsets)

    def testNoOffsets(self):
        offsets = StringIO('')
        ext = SubsequenceExtractor(offsets)
        self.assertEqual([], ext.offsets)

    def testSingleOffset(self):
        offsets = StringIO('3')
        ext = SubsequenceExtractor(offsets)
        self.assertEqual([(2, 3)], ext.offsets)

    def testSimpleRange(self):
        offsets = StringIO('3-5')
        ext = SubsequenceExtractor(offsets)
        self.assertEqual([(2, 5)], ext.offsets)

    def testTwoRanges(self):
        offsets = StringIO('3-5\n7-10')
        ext = SubsequenceExtractor(offsets)
        self.assertEqual([(2, 5), (6, 10)], ext.offsets)

    def testTwoRangesAndOneSingleOffset(self):
        offsets = StringIO('3-5\n20\n7-10')
        ext = SubsequenceExtractor(offsets)
        self.assertEqual([(2, 5), (19, 20), (6, 10)], ext.offsets)


class TestExtraction(TestCase):
    """
    Tests for the TestExtractor class when we ask it to extract something.
    """

    def testSimpleRange(self):
        offsets = StringIO('3-5')
        ext = SubsequenceExtractor(offsets)
        result = list(ext.extract('ACGTACAC'))
        self.assertEqual([(2, 5, 'GTA')], result)

    def testSequenceLongerThanOffsets(self):
        offsets = StringIO('3-500')
        ext = SubsequenceExtractor(offsets)
        result = list(ext.extract('ACGTACAC'))
        self.assertEqual([], result)
