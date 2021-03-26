#!/usr/bin/env python3

import re
from typing import List


def filter_datum(
            fields: list,
            redaction: str,
            message: str,
            separator: str
        ) -> str:
    """
    returns the log message
    """
    for fld in fields:
        message = re.sub(f'(?<={fld}=).*?(?={separator})', redaction, message)

    return message
