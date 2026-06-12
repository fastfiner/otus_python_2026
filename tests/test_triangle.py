import pytest
from src import Triangle


@pytest.fixture
def trian():
    return Triangle(3, 5, 4)

def test_triangle_area(trian):
    assert trian.get_area == 6, f"Ожидалось 6, получено {trian.get_area}"


def test_triangle_perimeter(trian):
    assert trian.get_perimeter == 12, (
        f"Ожидалось 12, получено {trian.get_area}"
    )


@pytest.mark.parametrize("a,b,c", [
    (3, 0, 2), (0, 3, 2), (2, 3, 0),
    (3, -1, 3), (-1, 4, 3), (4, 3, -1),
    (1, 1, 3), (1, 3, 1), (3, 1, 1)
])
def test_triangle_negative_sides(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)
