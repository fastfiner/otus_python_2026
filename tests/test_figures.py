import pytest
from src import Rectangle, Square, Circle, Triangle


# Rectangle
def test_rectangle_area():
    rect = Rectangle(3, 5)
    assert rect.get_area == 15, f"Ожидалось 15, получено {rect.get_area}"


def test_rectangle_perimeter():
    rect = Rectangle(3, 5)
    assert rect.get_perimeter == 16, f"Ожидалось 16, получено {rect.get_area}"


@pytest.mark.parametrize("a,b", [
    (3, 0), (0, 3), (0, 0),
    (3, -1), (-1, 3), (-1, -1)
])
def test_rectangle_negative_sides(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)


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


# Triangle
def test_triangle_area():
    trian = Triangle(3, 5, 4)
    assert trian.get_area == 6, f"Ожидалось 6, получено {trian.get_area}"


def test_triangle_perimeter():
    trian = Triangle(3, 5, 4)
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
