import re


class InvalidLccnError(Exception):
    pass


def normalize(lccn):
    """Normalize LCCN according to Library of Congress rules
    (https://www.loc.gov/marc/lccn-namespace.html)
  
    An LCCN is to be normalized to its canonical form described in the 
    syntax description above, as follows:
  
    1. Remove all blanks.
    2. If there is a forward slash (/) in the string, remove it, and remove 
       all characters to the right of the forward slash.
    3. If there is a hyphen in the string:
       * Remove it.
       * Inspect the substring following (to the right of) the (removed)
         hyphen. Then (and assuming that steps 1 and 2 have been carried 
         out):
         *  All these characters should be digits, and there should be six
            or less.
         *  If the length of the substring is less than 6, left-fill the
            substring with zeros until the length is six.
    """
    parts = lccn.replace(' ', '').split('/')[0].split('-', 2)

    if len(parts) == 1:
        return parts[0]

    if re.match(r'^\d{1,6}$', parts[1]):
        return parts[0] + parts[1].rjust(6, '0')

    raise InvalidLccnError(
        "%s is not a valid LCCN " % lccn +
        "(part to the right of hyphen should be 6 numeric characters " +
        "or fewer")


def is_valid(lccn):
    """Validate LCCN according to Library of Congress rules
    (https://www.loc.gov/marc/lccn-namespace.html)
  
    A normalized LCCN is a character string eight to twelve characters in
    length. (For purposes of this description characters are ordered from 
    left to right -- "first" means "leftmost".)
  
    * The rightmost eight characters are always digits.
    * If the length is 9, then the first character must be alphabetic.
    * If the length is 10, then the first two characters must be either both
      digits or both alphabetic.
    * If the length is 11, then the first character must be alphabetic and 
      the next two characters must be either both digits or both alphabetic.
    * If the length is 12, then the first two characters must be alphabetic 
      and the remaining characters digits.
    """
    if re.match(r'^([A-z]{2}\d{2}|([A-z]?([A-z]{2}|\d{2}))|[A-z])?\d{8}$',
                lccn):
        return True

    return False
