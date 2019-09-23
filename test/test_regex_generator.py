import pytest
from regex_engine import generator
@pytest.mark.parametrize(
    "start_range, end_range, expected_regex", [
        (25, 53, '^([3-4][0-9]|2[5-9]|5[0-3])$'),
        (-14, 18, '^(-[1-9]|-1[0-4]|[0-9]|1[0-8])$'),
        (5.98, 21.2, '^([6-8]\\.[0-9][0-9]?[0-9]*|5\\.9[8-9]?[0-9]*|9\\.[0-8][0-9]?[0-9]*|9\\.9[0-9]?[0-9]*|1[1-9]\\.[0-9][0-9]?[0-9]*|10\\.[1-9][0-9]?[0-9]*|10\\.0[0-9]?[0-9]*|2[0-0]\\.[0-9][0-9]?[0-9]*|21\\.[0-1][0-9]?[0-9]*|21\\.2[0-0]?[0-9]*)$')
    ]
)
def test_numerical_range(start_range, end_range, expected_regex):
    generate = generator()
    generated_regex = generate.numerical_range(start_range, end_range)
    assert generated_regex == expected_regex

# pipenv run python -m pytest test/test_regex_generator.py -v --maxfail=1