class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        num = self.number

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        return result



num = int(input("Enter a number (1-3999): "))
converter = RomanConverter(num)
print("Roman numeral:", converter.to_roman())
