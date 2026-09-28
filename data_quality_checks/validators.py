"""Simple data-validation functions for checking individual records."""

import re

# A deliberately simple pattern: something@something.something, no spaces.
# Real-world email validation is much messier; this catches obvious mistakes.
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def check_required_fields(record: dict, required: list[str]) -> list[str]:
    """Return the required fields that are missing or empty in the record.

    An empty list means the record passed.
    """
    missing = []
    for field in required:
        value = record.get(field)
        if value is None or (isinstance(value, str) and value.strip() == ""):
            missing.append(field)
    return missing


def is_positive_number(value) -> bool:
    """Return True if value is a number (int or float) greater than zero."""
    # bool is a subclass of int in Python, so True would otherwise count as 1.
    if isinstance(value, bool):
        return False
    if not isinstance(value, (int, float)):
        return False
    return value > 0


def is_valid_email(value) -> bool:
    """Return True if value looks like an email address."""
    if not isinstance(value, str):
        return False
    return bool(EMAIL_PATTERN.match(value.strip()))
