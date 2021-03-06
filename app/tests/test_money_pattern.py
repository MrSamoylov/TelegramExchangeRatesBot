import re
import unittest

from app.libs.price import MONEY_PATTERN_EU, MONEY_PATTERN_US, MONEY_PATTERN


US_GOOD_CASES = [
    '1,000.0001',
    '1,000.01',
    '1,000,000.01',
    '1,000',
    '100,000',
    '100',
    '1000',
    '1000000',
    '1000000.01',
    '1.1',
    '0.1',
    '1.01',
    '10.0',
    '10.0001',
    '00.1',
    '000.1',
    f'{"0" * 12}.{"0" * 8}',
    f'{"0" * 12}.1',
    f'{"0" * 12}',
    f'{"1" * 12}.{"1" * 8}',
    f'111{",000" * 3}',
    f'1{",000" * 3}',
    f'1{",000" * 3}.{"1" * 8}',
]

EU_GOOD_CASES = [
    '1.000,0001',
    '1.000,01',
    '1.000.000,01',
    '1.000',
    '100.000',
    '100',
    '1000',
    '1000000',
    '1000000,01',
    '1,1',
    '0,1',
    '1,01',
    '10,0',
    '10,0001',
    '00,1',
    '000,1',
    f'{"0" * 12},{"0" * 8}',
    f'{"0" * 12},1',
    f'{"0" * 12}',
    f'{"1" * 12},{"1" * 8}',
    f'111{".000" * 3}',
    f'1{".000" * 3}',
    f'1{".000" * 3},{"1" * 8}',
]

BOTH_BAD_CASES = [
    '1.00.',
    '1.00.00',
    '1,00.00',
    '1.00,00',
    '1,00,00',
    '100,00,,',
    '100,00..',
    '10.0,00..',
    '.1',
    ',1',
    ' ',
    ',',
    ',',
    '',
    f'{"0"*13}.{"0"*8}',
    f'{"0"*13},{"0"*8}',
    f'{"0"*12}.{"0"*9}',
    f'{"0"*12},{"0"*9}',
    f'1111{",000" * 3}',
    f'1111{".000" * 3}',
    f'1{",000" * 4}',
    f'1{",000" * 4}.{"1" * 8}',
    f'1{".000" * 4}',
    f'1{".000" * 4},{"1" * 8}',
]

US_BAD_CASES = BOTH_BAD_CASES + [
    # EU
    '1.000,0001',
    '1.000,01',
    '1.000.000,01',
    '1000000,01',
    '1,1',
    '0,1',
    '1,01',
    '10,0',
    '10,0001',
    '00,1',
    '000,1',
    f'{"0" * 12},{"0" * 8}',
    f'{"0" * 12},1',
    f'{"1" * 12},{"1" * 8}',
    f'1{".000" * 3}',
    f'1{".000" * 3},{"1" * 8}',
]

EU_BAD_CASES = BOTH_BAD_CASES + [
    # US
    '1,000.0001',
    '1,000.01',
    '1,000,000.01',
    '1000000.01',
    '1.1',
    '0.1',
    '1.01',
    '10.0',
    '10.0001',
    '00.1',
    '000.1',
    f'{"0" * 12}.{"0" * 8}',
    f'{"0" * 12}.1',
    f'{"1" * 12}.{"1" * 8}',
    f'1{",000" * 3}',
    f'1{",000" * 3}.{"1" * 8}',
]


class MoneyPatternUSTest(unittest.TestCase):
    mpt = f'^({MONEY_PATTERN_US})$'

    def test_good(self):
        for case in US_GOOD_CASES:
            r = re.match(self.mpt, case)
            self.assertIsNotNone(r, case)
            self.assertEqual(r.group(1), case)

    def test_bad(self):
        for case in US_BAD_CASES:
            self.assertFalse(re.match(self.mpt, case))


class MoneyPatternEUTest(unittest.TestCase):
    mpt = f'^({MONEY_PATTERN_EU})$'

    def test_good(self):
        for case in EU_GOOD_CASES:
            r = re.match(self.mpt, case)
            self.assertIsNotNone(r, case)
            self.assertEqual(r.group(1), case)

    def test_bad(self):
        for case in EU_BAD_CASES:
            self.assertFalse(re.match(self.mpt, case))


class MoneyPatternTest(unittest.TestCase):
    mpt = f'^({MONEY_PATTERN})$'

    def test_good(self):
        for case in US_GOOD_CASES + EU_GOOD_CASES:
            r = re.match(self.mpt, case)
            self.assertIsNotNone(r, case)
            self.assertEqual(r.group(1), case)

    def test_bad(self):
        for case in BOTH_BAD_CASES:
            self.assertFalse(re.match(self.mpt, case))
