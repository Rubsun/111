import pytest

from taskkk import get_degree
test_data = [
    ((1.0, 3.5, 4.5, 0), 139.215),
    ((1, 1, 1, 1), 85.944), 
    ((1.2, 13.2, 1.9, 19.2), 204.248),
]

@pytest.mark.parametrize('input_data, expected', test_data)
def test_get_degree(input_data, expected):
    """
    Тест на нахождение градусной меры точки соприкосновения через время
    """
    r, t, a, v = input_data
    result = get_degree(r, t, a, v)
    assert result == expected