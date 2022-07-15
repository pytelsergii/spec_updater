import pytest
from utils import str_utils


@pytest.mark.parametrize('test_data, expected_result', [
    ('20&nbsp;699', 20699.0), (' 7 865,00 грн ', 7865), ('1500 грн.', 1500), ('25.19', 25.19), ('chars', 0)])
def test_str_price_to_float(test_data, expected_result):
    assert str_utils.str_price_to_float(test_data) == expected_result, 'Price incorrectly converted'
