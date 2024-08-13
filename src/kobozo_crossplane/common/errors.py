"""
Module containing custom exception classes for the NgxParser.

This module defines a set of exceptions used for error handling in the
NgxParser. The exceptions cover a variety of parsing errors, including
syntax errors, directive errors, and more specific cases such as
argument errors, context errors, and unknown directive errors.
"""

from __future__ import annotations


class NgxParserBaseError(Exception):
    """
    Base exception class for NgxParser-related errors.

    Attributes
    ----------
        strerror (str): Description of the error.
        filename (str): Name of the file where the error occurred.
        lineno (int | None): Line number in the file where the error occurred.

    """

    def __init__(self: NgxParserBaseError, strerror: str, filename: str, lineno: int | None) -> None:
        """
        Initialize the exception with error details.

        Args:
        ----
            strerror (str): Description of the error.
            filename (str): Name of the file where the error occurred.
            lineno (int | None): Line number in the file where the error occurred, or None if not applicable.

        """
        self.args = (strerror, filename, lineno)
        self.filename = filename
        self.lineno = lineno
        self.strerror = strerror

    def __str__(self: NgxParserBaseError) -> str:
        """
        Return a string representation of the error.

        Returns
        -------
            str: Formatted error message including the filename and line number.

        """
        if self.lineno is not None:
            return "{} in {}:{}".format(*self.args)

        return "{} in {}".format(*self.args)


class NgxParserSyntaxError(NgxParserBaseError):
    """Exception raised for syntax errors in the NgxParser."""



class NgxParserDirectiveError(NgxParserBaseError):
    """Exception raised for directive-related errors in the NgxParser."""



class NgxParserDirectiveArgumentsError(NgxParserDirectiveError):
    """Exception raised for errors related to directive arguments in the NgxParser."""



class NgxParserDirectiveContextError(NgxParserDirectiveError):
    """Exception raised for errors related to directive context in the NgxParser."""



class NgxParserDirectiveUnknownError(NgxParserDirectiveError):
    """Exception raised for unknown directive errors in the NgxParser."""

