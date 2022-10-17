from validation.integer.params import IntegerValidationParams

from validation.integer.validator import IntegerValidator

if __name__ == '__main__':
    params = IntegerValidationParams(
        space=' ',
        signs=['+', '-'],
        numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        enter='$',
    )

    inp = str(input('input number: '))

    validator = IntegerValidator(params)

    validator.validate(inp + params.enter)
