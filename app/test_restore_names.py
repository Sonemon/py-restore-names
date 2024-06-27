import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"}
        ),
        (
            {"last_name": "Adams",
             "full_name": "Mike Adams"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}
        )
    ]
)
def test_restore_names(
        test_input: dict,
        expected: dict
) -> None:
    restore_names([test_input])
    assert test_input == expected
