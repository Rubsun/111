import pytest
from Theasure_map import theasure_map


test_date = (
    (
        [
            [0, 0, 't'],
            [0, 0, 0],
            ['x', 0, 0],
        ], 'EENN'
    ),
    (
        [
            ['', '', 'x'],
            ['', '', ''],
            ['', '', 't'],
        ], 'SS'
    ),
    (
        [
            ['x', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', 't', '', '', ''],
        ], 'EESSSS'
    )

)

@pytest.mark.parametrize('th_map, expected', test_date)
def test_get_path(th_map: list, expected: str):
    assert sorted(theasure_map(th_map)) == sorted(expected)
    
