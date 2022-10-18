from validation.float.params import FloatValidationParams


class FloatValidator:
    def __init__(self, params: FloatValidationParams):
        self.params = params
        self.negative = False
        self.number = 0
        self.k = 10

    def __initialize__(self):
        self.negative = False
        self.number = 0
        self.k = 10

    def validate(self, inp: str):
        self.__initialize__()
        for i in range(len(inp)):
            if inp[i] == self.params.space:
                continue
            elif inp[i] in self.params.signs:
                if inp[i] == '-':
                    self.negative = True
                return self.__sign(inp[i + 1:])
            elif inp[i] == self.params.comma:
                return self.__comma(inp[i + 1:])
            elif inp[i] in self.params.numbers:
                self.__calculate_left(int(inp[i]))
                return self.__left_num(inp[i + 1:])

            return self.__err('symbol ' + inp[i] + ' not a number or sign')

        self.__err('empty input')

    def __sign(self, inp: str):
        for i in range(len(inp)):
            if inp[i] not in self.params.numbers:
                return self.__err('not number after sign')
            self.__calculate_left(int(inp[i]))
            return self.__left_num(inp[i + 1:])

    def __err(self, reason: str):
        raise BaseException('error: ' + reason)

    def __comma(self, inp: str):
        for i in range(len(inp)):
            if inp[i] in self.params.numbers:
                self.__calculate_right(int(inp[i]))
                return self.__right_num(inp[i + 1:])
            return self.__err('symbol ' + inp[i] + ' not a number')

    def __left_num(self, inp: str):
        for i in range(len(inp)):
            if inp[i] in self.params.numbers:
                self.__calculate_left(int(inp[i]))
                continue
            elif inp[i] == self.params.comma:
                return self.__comma(inp[i + 1:])
            elif inp[i] == self.params.enter:
                return self.__end()
            return self.__err('symbol ' + inp[i] + ' not a number or comma')

    def __right_num(self, inp: str):
        for i in range(len(inp)):
            if inp[i] in self.params.numbers:
                self.__calculate_right(int(inp[i]))
                continue
            if inp[i] == self.params.enter:
                return self.__end()
            return self.__err('symbol ' + inp[i] + ' not a number')

    def __end(self):
        print('number validate success')

    def __calculate_left(self, inp: int):
        self.number = self.number * 10 + (-inp if self.negative else inp)

    def __calculate_right(self, inp: int):
        self.number = self.number + (-inp / self.k if self.negative else inp / self.k)
        self.k *= 10
