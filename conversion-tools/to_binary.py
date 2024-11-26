"""
Convert number to binary
"""

from stacks import stack


class BinaryStack(stack.Stack):
    """child class"""

    def __str__(self):
        """print values"""
        return ''.join(reversed(self._items))


def decimal_binary(n: int) -> str:
    """
    Convert n (decimal) to binary string

    >>> decimal_binary(42)
    '101010'
    """
    s = BinaryStack()
    while n > 0:
        i = n % 2
        s.push(str(i))

        n //= 2

    return str(s)


def binary_decimal(n: str) -> int:
    """
    Convert binary string to decimal

    >>> binary_decimal('101010')
    42
    """
    k = len(n) - 1

    dec = 0

    for i in n:
        dec += (int(i) * (2 ** k))
        k -= 1

    return dec
