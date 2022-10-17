from validation.float.params import FloatValidationParams

from validation.float.validator import FloatValidator

if __name__ == '__main__':
    params = FloatValidationParams(
        space=' ',
        signs=['+', '-'],
        numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        comma='.',
        enter='$',
    )

    inp = str(input('input number: '))

    validator = FloatValidator(params)

    validator.validate(inp + params.enter)

    print(validator.number)
