#
from .converter import AsBoolConverter


DEFAULT_TRUE_VALUES = (
    't',
    'true',
    'y',
    'yes',
)

DEFAULT_FALSE_VALUES = (
    'f',
    'false',
    'n',
    'no',
)

asbool = AsBoolConverter(DEFAULT_TRUE_VALUES,
                         DEFAULT_FALSE_VALUES)
