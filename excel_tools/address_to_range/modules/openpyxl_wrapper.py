from openpyxl.utils.cell import coordinate_from_string, get_column_letter, column_index_from_string


def get_col_letter(num: int) -> str:
    """列番号から列アルファベットに変換する"""
    return get_column_letter(num)


def coord_from_str(addr: str) -> tuple[str, int]:
    """セルアドレスを列と行に分割する"""
    return coordinate_from_string(addr)


def col_idx_from_str(col: str) -> int:
    """列アルファベットを数値に変換する"""
    return column_index_from_string(col)
