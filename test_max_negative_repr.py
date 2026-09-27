from unittest import TestCase, main
from intro import max_negative_repr

class TestMaxNegativeRepr(TestCase):
    def test_largest_pair(self):
        self.assertEqual(
            max_negative_repr([100, 4, 1, -1, -4, -100]),
            100,
        )

    def test_only_one_pair(self):
        self.assertEqual(
            max_negative_repr([100, 4, 1, -1]),
            1,
        )

    def test_no_pair(self):
        self.assertEqual(
            max_negative_repr([100, 4, 1, -2]),
            -1,
        )

    def test_empty_list(self):
        self.assertEqual(max_negative_repr([]), -1)


if __name__ == "__main__":
    main()