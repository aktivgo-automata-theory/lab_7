import unittest

from validation.integer.params import IntegerValidationParams
from validation.integer.validator import IntegerValidator


class TestIntegerValidator(unittest.TestCase):

    def setUp(self):
        self.params = IntegerValidationParams(
            space=' ',
            signs=['+', '-'],
            numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            enter='$',
        )
        self.validator = IntegerValidator(self.params)

    @unittest.expectedFailure
    def test_empty(self):
        self.assertEqual(None, self.validator.validate(''))

    @unittest.expectedFailure
    def test_empty_with_enter(self):
        self.assertEqual(None, self.validator.validate(''+self.params.enter))

    @unittest.expectedFailure
    def test_float(self):
        self.assertEqual(None, self.validator.validate('+2.1' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_1(self):
        self.assertEqual(None, self.validator.validate('+2 ' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_2(self):
        self.assertEqual(None, self.validator.validate('- 2' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_3(self):
        self.assertEqual(None, self.validator.validate('1 0' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_4(self):
        self.assertEqual(None, self.validator.validate('1g0' + self.params.enter))

    def test_positive_number(self):
        self.assertEqual(None, self.validator.validate('+2' + self.params.enter))

    def test_negative_number(self):
        self.assertEqual(None, self.validator.validate('-2' + self.params.enter))

    def test_success_1(self):
        self.assertEqual(None, self.validator.validate('100123' + self.params.enter))

    def test_success_2(self):
        self.assertEqual(None, self.validator.validate('      19' + self.params.enter))


if __name__ == '__main__':
    unittest.main()
