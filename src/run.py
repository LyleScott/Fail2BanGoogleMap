#!/usr/bin/env python
# Lyle Scott, III  // lyle@digitalfoo.net // Copyright 2013

import json
import os
import sys


#path = os.path.dirname(os.path.realpath(__file__))
#sys.path.insert(0, '%s/src' % path)

try:
    import constants
except ImportError:
    print '''Problem importing src/constants.py. Make sure
src/constants.py.sample is copied to src/constants.py and is setup
properly.'''
    sys.exit(3)

from parsers import ParserEmail
from parsers import ParserLog


def usage():
    """Usage statement."""
    me = sys.argv[0]
    print 'USAGE: %s' % me
    sys.exit(1)


def pre_checks():
    if not os.path.exists('src/constants.py'):
        print ('Copy constants.py.sample to constants.py and fill in the '
            'appropriate options.')
        exit(2)


def get_parsers():
    """Parse arguments."""
    objs = []

    if constants.getConstant('EMAIL_ENABLE'):
        objs.append(ParserEmail)

    if constants.getConstant('LOG_ENABLE'):
        objs.append(ParserLog)

    return objs


def run(args):
    """Do work."""
    pre_checks()

    allresults = []
    for parser in get_parsers():
        results = parser.run()
        allresults.extend(list(results or []))

    with open('locations.json', 'w') as fp:
        fp.write('var locations = ')
        json.dump(allresults, fp)
        fp.write(';')


if __name__ == '__main__':
    run(get_parsers())
