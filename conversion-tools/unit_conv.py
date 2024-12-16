"""
Converts a value from a unit to another (rudimentary)
Includes: Metric lengths (from mm to km) and imperial (inch, foot, yard, miles)

values are approximated
"""

_METRIC_LENGTH = ["mm", "cm", "dm", "m", "dam", "hm", "km"]
_IMPERIAL_LENGTH = {"in": 2.54, "ft": 30.48, "yd": 91.44, "mi": 160934.4}


def convert_unit(n: int, unit: str, unit2: str):
    """convert value from one unit to other (metric unit)

    Representational invariants:
    - unit and unit2 are valid abbreviations of length units (e.g. mm for milimetres)
    - unit and unit2 are in _METRIC_LENGTH and _IMPERIAL_LENGTH
    """
    cm_value = to_cm(n, unit)
    if isinstance(cm_value, str):
        return "Not a supported unit."

    if unit2 in _IMPERIAL_LENGTH:
        return cm_value / _IMPERIAL_LENGTH[unit2]
    elif unit2 in _METRIC_LENGTH:
        return cm_value / (10 ** (_METRIC_LENGTH.index(unit2) - 1))


def to_cm(n: int, unit: str):
    """dsfdsfdsfs"""

    if unit in _METRIC_LENGTH:
        return n * (10 ** (_METRIC_LENGTH.index(unit) - 1))
    elif unit in _IMPERIAL_LENGTH:
        return n * _IMPERIAL_LENGTH[unit]
    else:
        return "Error"
