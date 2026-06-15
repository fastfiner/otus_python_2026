import pytest
from src import Square

# Square
def test_square_area():
    squa = Square(5)
    assert squa.get_area == 25, f"Ожидалось 25, получено {squa.get_area}"


def test_square_perimeter():
    squa = Square(5)
    assert squa.get_perimeter == 20, f"Ожидалось 20, получено {squa.get_area}"


@pytest.mark.parametrize("a", [
    (0), (-1)
])
def test_square_negative_sides(a):
    with pytest.raises(ValueError):
        Square(a)
