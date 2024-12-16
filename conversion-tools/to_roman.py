"""
convert to roman numerals
"""


def thousands(n):
    """return thousands part"""
    stmt = ""
    for x in range(0, n, 1):
        stmt += "M"

    return stmt


def hundreds(n):
    """return hundreds part"""
    if n == 9:
        return "CM"
    elif n >= 5:
        stmt = "D"
        for _ in range(0, n - 5, 1):
            stmt += "C"
        return stmt
    elif n == 4:
        return "CD"
    elif 0 < n < 4:
        stmt = ""
        for _ in range(0, n, 1):
            stmt += "C"
        return stmt

    return ""


def tens(n):
    """return tens part"""
    if n == 9:
        return "XC"
    elif n >= 5:
        stmt = "L"
        for _ in range(0, n - 5, 1):
            stmt += "X"
        return stmt
    elif n == 4:
        return "XL"
    elif n < 4 and n > 0:
        stmt = ""
        for _ in range(0, n, 1):
            stmt += "X"
        return stmt

    return ""


def ones(n):
    """return ones part"""
    if n == 9:
        return "IX"
    elif n >= 5:
        stmt = "V"
        for _ in range(0, n - 5, 1):
            stmt += "I"
        return stmt
    elif n == 4:
        return "IV"
    elif 0 < n < 4:
        stmt = ""
        for _ in range(0, n, 1):
            stmt += "I"
        return stmt

    return ""


def to_roman(n: int) -> str:
    """Convert n to their roman numeral equivalent.

    Preconditions:
    - 0 <= n <= 4000
    """
    num = n // 1  # num is not an alias

    th = thousands(num // 1000)
    num %= 1000

    hun = hundreds(num // 100)
    num %= 100

    t = tens(num // 10)
    num %= 10

    o = ones(num)

    return th + hun + t + o
