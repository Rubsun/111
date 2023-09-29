import pytest

from shorten_dir import shorten_direction

test_dirs = (
    ('',''),
    ('NN','NN'),
    ('NS', '')
)
@pytest.mark.parametrize('dirs, expected', test_dirs)
def test(dirs: str, expected: str):
    assert shorten_direction(dirs) == expected