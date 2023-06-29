# Excelのセル番地をセル範囲に変換する

## 概要

例えば、`["A1", "A2", "B1"]`という複数のセルアドレスが渡されたら、`["A1:A2", "B1:B1"]`に変換する。  
先に同じ列のセルアドレスを結合する処理の関係上、`["A1:B1", "A2:A2"]`にはなり得ない。  

このあたりの要領はテストを見てもらった方が分かりやすいかも。  
  
## 使い方  

```python
import address_to_range

print(address_to_range.convert_address_to_range(["A1", "A2", "B1"]))
```
