import numpy as np
import pytest

from sdia_python.lab2.ball_window import BallWindow


@pytest.mark.parametrize(
    "centre,radius, expected",
    [
        (np.array([[0, 0]]), 5, "BallWindow with center: [0 0] and radius: 5"),
        (np.array([[1, 5, 5]]), 10, "BallWindow with center: [1 5 5] and radius: 10"),
    ],
)
def test_ball_string_representation(centre, radius, expected):
    assert str(BallWindow(centre, radius)) == expected


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.fixture
def ball_2d():
    return BallWindow(np.array([5, 5]), 5)


def test_len(ball_2d):
    assert len(ball_2d) == 2


def test_dimension(ball_2d):
    assert ball_2d.dimension() == 2


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([5, 5]), True),
        (np.array([0, 5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(ball_2d, point, expected):
    is_in = ball_2d.indicator_function(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([5, 5]), True),
        (np.array([0, 5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains(ball_2d, point, expected):
    is_in = point in ball_2d
    assert is_in == expected


@pytest.mark.parametrize(
    "center, rayon, expected", [(np.array([0, 0]), 1, np.pi),],
)
def test_volume(center, rayon, expected):
    assert BallWindow(center, rayon).volume() == expected
