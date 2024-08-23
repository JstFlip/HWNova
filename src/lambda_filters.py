import random
import string
from datetime import datetime


def generator() -> str:
    """
    Generate a random string in size of 1-15 characters.
    """
    return "".join(random.choices(string.ascii_letters + string.digits + "-_.", k=random.randint(1, 15)))


def _is_valid_date(dt: str) -> bool:
    try:
        datetime.strptime(dt, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    strings = [generator() for _ in range(10)]
    strings.extend([  # Add some data, so we can then test filters easily below
        "2023-08-15",
        "5462346",
        "file1.csv",
        "file2.json",
        "2024-12-32"  # Invalid date
    ])

    int_only = list(filter(lambda x: x.isdigit(), strings))
    json_csv_end = list(filter(lambda x: x.endswith((".json", ".csv")), strings))
    iso_dates = list(filter(lambda x: _is_valid_date(x), strings))

    print(f"Original strings: {strings}")
    print(f"Filtered only integers: {int_only}")
    print(f"Filtered only ending with .json/.csv: {json_csv_end}")
    print(f"Filtered only valid ISO dates: {iso_dates}")
