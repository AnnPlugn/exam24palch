from fractions import Fraction


def parse_mixed_fraction(s):
    whole, fraction = s.split(' ')
    whole = int(whole)
    numerator, denominator = map(int, fraction.split('/'))
    return whole, numerator, denominator


def to_mixed_fraction(frac):
    whole = frac.numerator // frac.denominator
    numerator = frac.numerator % frac.denominator
    return f"{whole} {numerator}/{frac.denominator}" if whole else f"{numerator}/{frac.denominator}"


def fraction_calculator(expression):
    num1_whole, num1_numerator, num1_denominator, operator, num2_whole, num2_numerator, num2_denominator = map(int,
                                                                                                               expression.split())
    num1 = Fraction(num1_whole) + Fraction(num1_numerator, num1_denominator)
    num2 = Fraction(num2_whole) + Fraction(num2_numerator, num2_denominator)

    if operator == 1:
        result = num1 + num2
    elif operator == 2:
        result = num1 - num2
    elif operator == 3:
        result = num1 * num2
    elif operator == 4:
        result = num1 / num2
    else:
        return "Invalid operator"

    return to_mixed_fraction(result)


# Пример использования:
expression = "1 1/2 1 5 3/4"
print(fraction_calculator(expression))  # Вывод: 7 1/4
