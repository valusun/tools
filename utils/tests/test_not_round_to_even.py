from decimal import Decimal
import pytest
from .. import not_round_to_even


class Test_Round:
    @pytest.mark.parametrize(
        "val, dig, res",
        [
            ("0.4", 0, 0.0),
            ("0.5", 0, 1.0),
            ("0.6", 0, 1.0),
            ("0.44", 1, 0.4),
            ("0.45", 1, 0.5),
            ("0.46", 1, 0.5),
            ("0", 0, 0),
        ],
    )
    def test_PositiveDecimalNumber(self, val, dig, res):
        assert not_round_to_even.Round(Decimal(val), dig) == Decimal(str(res))

    @pytest.mark.parametrize(
        "val, dig, res",
        [
            ("-0.4", 0, 0.0),
            ("-0.5", 0, -1.0),
            ("-0.6", 0, -1.0),
            ("-0.44", 1, -0.4),
            ("-0.45", 1, -0.5),
            ("-0.46", 1, -0.5),
            ("-0", 0, 0),
        ],
    )
    def test_NegativeDecimalNumber(self, val, dig, res):
        assert not_round_to_even.Round(Decimal(val), dig) == Decimal(str(res))

    @pytest.mark.parametrize(
        "val, dig, res",
        [
            (14, -1, 10),
            (15, -1, 20),
            (16, -1, 20),
            (140, -2, 100),
            (150, -2, 200),
            (160, -2, 200),
        ],
    )
    def test_PositiveIntegerNumber(self, val, dig, res):
        assert not_round_to_even.Round(val, dig) == res

    @pytest.mark.parametrize(
        "val, dig, res",
        [
            (-14, -1, -10),
            (-15, -1, -20),
            (-16, -1, -20),
            (-140, -2, -100),
            (-150, -2, -200),
            (-160, -2, -200),
        ],
    )
    def test_NegativeIntegerNumber(self, val, dig, res):
        assert not_round_to_even.Round(val, dig) == res
