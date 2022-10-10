space = ' '
signs = ['+', '-']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
enter = '$'


def s(inp: str):
    for i in range(len(inp)):
        if inp[i] == space:
            continue
        elif inp[i] in signs:
            return sign(inp[i + 1:])
        elif inp[i] in numbers:
            return num(inp[i + 1:])

        return err('symbol ' + inp[i] + ' not a number or sign')


def sign(inp: str):
    for i in range(len(inp)):
        if inp[i] not in numbers:
            return err('not number after sign')
        return num(inp[i + 1:])


def err(reason: str):
    raise BaseException('error: ' + reason)


def num(inp: str):
    for i in range(len(inp)):
        if inp[i] in numbers:
            continue
        if inp[i] == enter:
            return end()
        return err('symbol ' + inp[i] + ' not a number')


def end():
    print('number validate success')


if __name__ == '__main__':
    inp = str(input('input number: '))
    s(inp + enter)
