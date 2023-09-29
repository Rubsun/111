import pytest
from checking_numbers import check_phone

valid_phones = ('+79282037102', '89182835744', '+79654837120', '81238746579')
invalid_phones = ('79282037102', '891828357441', '891828357', '89182as5744', '8 918 2835744')


@pytest.mark.parametrize('phone', valid_phones)
def test_valid_phone(phone: str):
    assert check_phone(phone)


@pytest.mark.parametrize('phone', invalid_phones)
def test_invalid_phone(phone: str):
    assert not check_phone(phone)
