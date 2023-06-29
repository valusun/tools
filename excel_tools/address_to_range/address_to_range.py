from collections import defaultdict
from itertools import groupby, count
from typing import DefaultDict


from .modules.openpyxl_wrapper import coord_from_str, get_col_letter, col_idx_from_str


def _compress_numbers(nums: list[int]) -> list[tuple[int, int]]:
    """連番の圧縮を行う

    Returns:
        list[tuple[int, int]]: (連番の先頭, 連番の最後)のタプル型のリスト

    Examples:
        >>> _compress_numbers([1, 2, 3, 4, 6])
        [(1, 4), (6, 6)]
    """
    compressed: list[tuple[int, int]] = []
    for _, group in groupby(sorted(nums), key=lambda n, c=count(): n - next(c)):
        g = list(group)
        s, e = g[0], g[-1]
        compressed.append((s, e))
    return compressed


def _merge_in_col(cells: list[str]) -> list[str]:
    """列方向へ結合しセル範囲を作成する(Examples参照)

    Args:
        cells (list[str]): 結合対象のセル。":"が含まれたセル範囲でなければならない。

    Returns:
        list[str]: 結合後のセル

    Examples:
        >>> _merge_in_col(["A1:A1", "A2:A2", "B1:B1"])
        ["A1:B1", "A2:A2"]
        >>> _merge_in_col(["A1:B1", "C1:C1", "A2:A2"])
        ["A1:C1", "A2:A2"]
    """
    rows_to_cols: DefaultDict[tuple[int, int], list[str]] = defaultdict(list)
    for cell in cells:
        start_addr, end_addr = cell.split(":")
        start_col, start_row = coord_from_str(start_addr)
        end_col, end_row = coord_from_str(end_addr)
        start_col_idx, end_col_idx = col_idx_from_str(start_col), col_idx_from_str(end_col)
        for c in range(start_col_idx, end_col_idx + 1):
            rows_to_cols[(start_row, end_row)].append(get_col_letter(c))
    merged: list[str] = []
    for (start_row, end_row), cols in rows_to_cols.items():
        col_indexes = [col_idx_from_str(c) for c in cols]
        compacted_col_indexes = _compress_numbers(col_indexes)
        for start, end in compacted_col_indexes:
            start_col, end_col = get_col_letter(start), get_col_letter(end)
            merged.append(f"{start_col}{start_row}:{end_col}{end_row}")
    return merged


def _merge_in_row(cells: list[str]) -> list[str]:
    """行方向へ結合しセル範囲を作成する(Examples参照)

    Args:
        cells (list[str]): 結合対象のセル。":"が含まれたセル範囲でなければならない。

    Returns:
        list[str]: 結合後のセル

    Examples:
        >>> _merge_in_row(["A1:A1", "A2:A2", "B1:B1"])
        ["A1:A2", "B1:B1"]
        >>> _merge_in_row(["A1:A2", "A3:A3", "B1:B1"])
        ["A1:A3", "B1:B1"]
    """
    cols_to_rows: DefaultDict[tuple[str, str], list[int]] = defaultdict(list)
    for cell in cells:
        start_addr, end_addr = cell.split(":")
        start_col, start_row = coord_from_str(start_addr)
        end_col, end_row = coord_from_str(end_addr)
        for row in range(start_row, end_row + 1):
            cols_to_rows[(start_col, end_col)].append(row)
    merged: list[str] = []
    for (start_col, end_col), rows in cols_to_rows.items():
        compacted_rows = _compress_numbers(rows)
        for start_row, end_row in compacted_rows:
            merged.append(f"{start_col}{start_row}:{end_col}{end_row}")
    return merged


def _to_rng(addresses: list[str]) -> list[str]:
    """セル範囲に変換する('A1'→'A1:A1')"""
    ret = []
    for ad in addresses:
        ret.append(ad if ":" in ad else f"{ad}:{ad}")
    return ret


def convert_address_to_range(addresses: list[str]) -> list[str]:
    """セルアドレスをセル範囲に変換する

    Args:
        addresses (list[str]): 変換対象のセルアドレス

    Returns:
        list[str]: 変換後のセル範囲
    """
    rngs = _to_rng(addresses)
    cells = _merge_in_row(rngs)
    cells = _merge_in_col(cells)
    # colを繋いだ後にrowを繋げられるパターンもあるため(イケてない)
    cells = _merge_in_row(cells)
    return cells
