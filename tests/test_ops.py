import unittest

from mylib import add, divide, multiply


class OpsTest(unittest.TestCase):
    def test_add(self) -> None:
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_multiply(self) -> None:
        assert multiply(2, 3) == 6
        assert multiply(-1, 1) == -1
        assert multiply(0, 5) == 0

    def test_divide(self) -> None:
        assert divide(6, 2) == (3, 0)
        assert divide(7, 2) == (3, 1)
        assert divide(0, 5) == (0, 0)


if __name__ == "__main__":
    unittest.main()
