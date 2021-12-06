from main import VentLine
import pytest

test_lines = [
        (
            VentLine(
                (0, 0),
                (0, 3)
            ),
            [(0,0), (0,1), (0,2), (0,3)]
        ),
        (
            VentLine(
                (0, 0),
                (3, 0)
            ),
            [(0,0), (1,0), (2,0), (3,0)]
        ),
        (
            VentLine(
                (0, 0),
                (3, 3),
                diag=True
            ),
            [(0,0), (1,1), (2,2), (3,3)]
        ),
        (
            VentLine(
                (3,0),
                (0,0)
            ),
            [(3,0), (2,0), (1,0), (0,0)]
        )
]

@pytest.mark.parametrize("line, expected", test_lines)
def test_line_points(line, expected):
    assert set(line.line_points()) == set(expected)


@pytest.mark.parametrize("line1, line2, expected", 
    [
        (
            VentLine(
                (0, 1),
                (0, 3)
            ),
            VentLine(
                (0, 2),
                (3, 2)
            ),
            [(0,2)]
        ),
        (
            VentLine(
                (0, 1),
                (0, 3)
            ),
            VentLine(
                (0, 2),
                (0, 4)
            ),
            [(0,2), (0,3)]
        ),
    ]
)
def test_line_intersections(line1, line2, expected):
    assert set(line1.get_intersection(line2)) == set(expected)


def test_no_intersections():
    line1 = VentLine(
        (0, 1),
        (0, 3)
    )
    line2 = VentLine(
        (3, 2),
        (3, 3)
    )
    assert not list(line1.get_intersection(line2))