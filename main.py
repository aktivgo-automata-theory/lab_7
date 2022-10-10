from validation.params import ValidationParams

from validation.integer.validator import IntegerValidator

if __name__ == '__main__':
    params = ValidationParams(
        space=' ',
        signs=['+', '-'],
        numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        enter='$',
    )

    inp = str(input('input number: '))

    integer_validator = IntegerValidator(params)

    integer_validator.start(inp + params.enter)
