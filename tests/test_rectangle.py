import pytest
from src import Rectangle


@pytest.fixture
def rect():
    return Rectangle(3, 5)


def test_rectangle_area(rect):
    assert rect.get_area == 15, f"Ожидалось 15, получено {rect.get_area}"


def test_rectangle_perimeter(rect):
    assert rect.get_perimeter == 16, f"Ожидалось 16, получено {rect.get_area}"


@pytest.mark.parametrize("a,b", [
    (3, 0), (0, 3), (0, 0),
    (3, -1), (-1, 3), (-1, -1)
])
def test_rectangle_negative_sides(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)
