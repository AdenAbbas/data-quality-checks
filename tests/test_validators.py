import pytest

from data_quality_checks import (
    check_required_fields,
    is_positive_number,
    is_valid_email,
)

# --- check_required_fields ---


def test_required_fields_all_present():
    record = {"id": 1, "name": "Aden", "email": "a@b.com"}
    assert check_required_fields(record, ["id", "name", "email"]) == []


def test_required_fields_reports_missing_and_empty():
    record = {"id": 1, "name": "   "}  # name is blank, email is absent
    assert check_required_fields(record, ["id", "name", "email"]) == ["name", "email"]


def test_required_fields_zero_is_not_missing():
    # 0 is a real value, not a missing one.
    assert check_required_fields({"count": 0}, ["count"]) == []


# --- is_positive_number ---


@pytest.mark.parametrize("value", [1, 0.5, 1_000_000])
def test_positive_numbers_pass(value):
    assert is_positive_number(value) is True


@pytest.mark.parametrize("value", [0, -1, -0.01, "5", None, True])
def test_non_positive_or_non_numbers_fail(value):
    assert is_positive_number(value) is False


# --- is_valid_email ---


@pytest.mark.parametrize("value", ["aden@example.com", "first.last@sub.domain.co.uk"])
def test_valid_emails_pass(value):
    assert is_valid_email(value) is True


@pytest.mark.parametrize(
    "value", ["", "no-at-sign.com", "two@@example.com", "a@b", "has space@x.com", None]
)
def test_invalid_emails_fail(value):
    assert is_valid_email(value) is False
