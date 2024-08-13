"""
Compatibility utilities for handling Python 2 and Python 3 differences.

This module provides functions and constants to ensure compatibility
between Python 2 and Python 3. It includes handling for input functions,
basestring compatibility, and workarounds for changes introduced in
Python 3.7, such as PEP 479.
"""

import functools
import sys
from typing import Any, Callable, Generator

PY2 = (sys.version_info[0] == 2) # noqa: PLR2004
PY3 = (sys.version_info[0] >= 3) # noqa: PLR2004

if PY2:
    input = raw_input # noqa: A001, F821
    basestring = basestring # noqa: F821, PLW0127
else:
    input = input # noqa: PLW0127, A001
    basestring = str


def fix_pep_479(generator: Callable) -> Callable:
    """
    Address Python 3.7's PEP 479 breaking crossplane's lexer.

    Read more here: https://www.python.org/dev/peps/pep-0479/
    """
    @functools.wraps(generator)
    def _wrapped_generator(*args: tuple, **kwargs: dict) -> Generator[Any, None, None]:
        try:
            yield from generator(*args, **kwargs)
        except RuntimeError:
            return

    return _wrapped_generator
