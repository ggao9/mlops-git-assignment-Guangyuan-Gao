import pandas as pd
import re

def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    if df.empty:
        raise ValueError("CSV file is empty")

    return df

def clean_phone(phone):
    if phone is None:
        return None

    phone = str(phone).strip()
    digits = re.sub(r"\D", "", phone)
    return digits

def validate_email(email):
    if email is None:
        return False

    email = email.strip()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))