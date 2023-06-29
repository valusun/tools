import pytest

from .. import address_to_range


class Test_compress_numbers:
    @pytest.mark.parametrize(
        "nums, result",
        [
            [[1, 2, 3], [(1, 3)]],
            [[1, 2, 4], [(1, 2), (4, 4)]],
            [[1, 3, 5], [(1, 1), (3, 3), (5, 5)]],
            [[0], [(0, 0)]],
        ],
    )
    def test_compress_numbers(self, nums, result):
        assert address_to_range._compress_numbers(nums) == result


class Test_merge_in_col:
    @pytest.mark.parametrize(
        "addresses, result",
        [
            [["A1:A1", "A2:A2", "B1:B1"], ["A1:B1", "A2:A2"]],
            [["A1:A2", "B1:B1"], ["A1:A2", "B1:B1"]],
            [["A1:B1", "C1:C1", "D1:D1"], ["A1:D1"]],
            [["B2:C3", "D2:F3", "G2:H4"], ["B2:F3", "G2:H4"]],
            [["Z1:Z1", "AA1:AB1", "AC1:AC1"], ["Z1:AC1"]],
        ],
    )
    def test_merge_in_col(self, addresses, result):
        assert address_to_range._merge_in_col(addresses) == result


class Test_merge_in_row:
    @pytest.mark.parametrize(
        "addresses, result",
        [
            [["A1:A1", "A2:A2", "B1:B1"], ["A1:A2", "B1:B1"]],
            [["A1:B1", "A2:A2"], ["A1:B1", "A2:A2"]],
            [["A1:A2", "A3:A3", "A4:A4"], ["A1:A4"]],
            [["B2:C3", "B4:C5", "B6:D7"], ["B2:C5", "B6:D7"]],
        ],
    )
    def test_merge_in_row(self, addresses, result):
        assert address_to_range._merge_in_row(addresses) == result


class Test_to_rng:
    @pytest.mark.parametrize(
        "addresses, result", [[["A1", "A2", "A3:A4"], ["A1:A1", "A2:A2", "A3:A4"]]]
    )
    def test_to_rng(self, addresses, result):
        assert address_to_range._to_rng(addresses) == result


class Test_convert_address_to_range:
    @pytest.mark.parametrize(
        "addresses, result",
        [
            [["A1", "A2", "B1"], ["A1:A2", "B1:B1"]],
            [["Z1", "AA1", "Z2:AA2"], ["Z1:AA2"]],
            [["Z1", "Z2", "AA1:AA2"], ["Z1:AA2"]],
        ],
    )
    def test_convert_address_to_range(self, addresses, result):
        assert address_to_range.convert_address_to_range(addresses) == result
