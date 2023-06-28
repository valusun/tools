from decimal import Decimal, ROUND_HALF_UP


def Round(number: Decimal | int, ndigit: int = 0) -> Decimal | int:
    """偶数丸めを考慮しない四捨五入を行う

    Notes:
        組み込み関数の`round`とほぼ同じ仕様
    """

    if ndigit == 0:
        digit = "0"
    elif ndigit > 0:
        digit = f"0.{'0'*(ndigit-1)}1"
    else:
        digit = f"1E{abs(ndigit)}"
    ret = Decimal(number).quantize(Decimal(digit), rounding=ROUND_HALF_UP)
    return int(ret) if ndigit <= 0 else ret
