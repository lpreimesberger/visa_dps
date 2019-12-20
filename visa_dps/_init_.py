# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import requests
import logging
import warnings
from logging import NullHandler
from .exceptions import FileModeWarning
from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __author__, __author_email__, __license__
from .__version__ import __copyright__, __cake__
from . import utils


def check_compatibility(requests_version):
    return True


# Check imported dependencies for compatibility.
try:
    check_compatibility(requests.__version__)
except (AssertionError, ValueError):
    print("Unsupported version of a support library ")


logging.getLogger(__name__).addHandler(NullHandler())
# FileModeWarnings go off per the default.
warnings.simplefilter('default', FileModeWarning, append=True)
