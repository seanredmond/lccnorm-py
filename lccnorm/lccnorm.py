import re

class InvalidLccnError(Exception):
    pass

def normalize(lccn):
    parts = lccn.replace(' ', '').split('/')[0].split('-', 2)

    if len(parts) == 1:
        return parts[0]

    if re.match(r'^\d{1,6}$', parts[1]):
        return parts[0] + parts[1].rjust(6, '0')

    raise InvalidLccnError(
        "%s is not a valid LCCN " % lccn + \
        "(part to the right of hyphen should be 6 numeric characters " + \
        "or fewer")


def is_valid(lccn):
    if re.match(r'^([A-z]{2}\d{2}|([A-z]?([A-z]{2}|\d{2}))|[A-z])?\d{8}$',
                lccn):
        return True

    return False
    
