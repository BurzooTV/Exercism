class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(' ', '')
        self.card_num = card_num

    def valid(self):
        if len(self.card_num) < 2 or not self.card_num.isdigit():
            return False

        return sum([(int(digit) * 2) % 10 + (int(digit) * 2) // 10 if index % 2 == 1 else int(digit) for index, digit in enumerate(self.card_num[::-1])]) % 10 == 0