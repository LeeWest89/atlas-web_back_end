#!/usr/bin/env python3
"""returns the log message obfuscated"""


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates the log depending on what needs to be redacted"""
    pattern = '(' + '|'.join(fields) + ')=[^' + re.escape(separator) + ']+'
    """
    Captures field names, with | as separator
    past the = gets values
    """
    hidden_message = re.sub(pattern, '\\1=' + redaction, message)
    """
    Makes substitutions to the pattern created in first variable,
    '\\1' passes field name ahead of the value that is being redacted
    """

    return (hidden_message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Stores list of fields"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """modifies the message useing filter_datum"""
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, record.msg, self.SEPARATOR)
        return (super().format(record))
