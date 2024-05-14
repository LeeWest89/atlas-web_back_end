#!/usr/bin/env python3
"""returns the log message obfuscated"""


import re


def filter_datum(fields, redaction, message, separator):
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
