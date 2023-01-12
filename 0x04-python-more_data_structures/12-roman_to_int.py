#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _sum = 0
    last = 0

    for letter in roman_string:
        if last == 0 or last >= roman[letter]:
            _sum += roman[letter]
        elif last < roman[letter]:
            _sum += roman[letter] - (last * 2)
        last = roman[letter]

    return _sum
