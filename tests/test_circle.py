import pytest
from src import Circle


# Circle
def test_circle_area():
    circ = Circle(10)
    assert circ.get_area == 314.159, (
        f"Ожидалось 314.159, получено {circ.get_area}"
    )


def test_circle_perimeter():
    circ = Circle(10)
    assert circ.get_perimeter == 62.8318, (
        f"Ожидалось 62.8318, получено {circ.get_area}"
    )


@pytest.mark.parametrize("a", [
    (0), (-1)
])
def test_circle_negative_sides(a):
    with pytest.raises(ValueError):
        Circle(a)
