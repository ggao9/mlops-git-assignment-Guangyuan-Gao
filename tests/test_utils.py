import pytest
from utils import load_csv, clean_phone, validate_email

def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("nonexistent.csv")

def test_clean_phone_various_formats():
    assert clean_phone("(123) 456-7890") == "1234567890"
    assert clean_phone("123.456.7890") == "1234567890"
    assert clean_phone("123-456-7890") == "1234567890"

def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid-email") is False