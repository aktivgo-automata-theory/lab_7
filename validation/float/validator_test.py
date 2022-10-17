import unittest

from validation.float.params import FloatValidationParams
from validation.float.validator import FloatValidator


class TestFloatValidator(unittest.TestCase):

    def setUp(self):
        self.params = FloatValidationParams(
            space=' ',
            signs=['+', '-'],
            numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            comma='.',
            enter='$',
        )
        self.validator = FloatValidator(self.params)

    @unittest.expectedFailure
    def test_empty(self):
        self.assertEqual(None, self.validator.validate(''))

    @unittest.expectedFailure
    def test_empty_with_enter(self):
        self.assertEqual(None, self.validator.validate(''+self.params.enter))

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
        self.assertEqual(None, self.validator.validate('1,0' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_5(self):
        self.assertEqual(None, self.validator.validate('10.' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_6(self):
        self.assertEqual(None, self.validator.validate('10.10 ' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_7(self):
        self.assertEqual(None, self.validator.validate('10.+ ' + self.params.enter))

    @unittest.expectedFailure
    def test_failure_8(self):
        self.assertEqual(None, self.validator.validate('1g0' + self.params.enter))

    def test_positive_number(self):
        self.assertEqual(None, self.validator.validate('+2.1' + self.params.enter))

    def test_negative_number(self):
        self.assertEqual(None, self.validator.validate('-2.3' + self.params.enter))

    def test_success_1(self):
        self.assertEqual(None, self.validator.validate('100123' + self.params.enter))

    def test_success_2(self):
        self.assertEqual(None, self.validator.validate('      19' + self.params.enter))

    def test_success_3(self):
        self.assertEqual(None, self.validator.validate('19.13' + self.params.enter))

    def test_success_4(self):
        self.assertEqual(None, self.validator.validate('-19.13' + self.params.enter))

    def test_success_5(self):
        self.assertEqual(None, self.validator.validate('-19' + self.params.enter))


if __name__ == '__main__':
    unittest.main()
