# Lccnorm

[![PyPi Version](https://badge.fury.io/py/lccnorm.svg)][pypi]
[![Build Status](http://img.shields.io/travis/seanredmond/lccnorm-py.svg)][travis]

[travis]: http://travis-ci.org/seanredmond/lccnorm-py
[pypi]: https://pypi.org/project/lccnorm/


## Installation

    pip install lccnorm
    
## Usage

Import the package

    >>> import lccnorm

Get a normalized version of an LCCN:

    >>> lccnorm.normalize("75-425165//r75")
    '75425165'
     
Check that an LCCN is valid:

    >>> Lccnorm.is_valid("75425165")
    True
    >>> lccnorm.is_valid("not even a number")
    False

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/seanredmond/lccnorm-py. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Lccnorm project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/seanredmond/lccnorm-py/blob/master/CODE_OF_CONDUCT.md).
