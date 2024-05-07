import pytest

from solution import Solution

sol = Solution()

@pytest.mark.parametrize(
        "a, b, c",
        [
            (2, 3, 5)
        ]
)
def test_F1(a, b, c):
    assert sol.F1_(a, b) == c
