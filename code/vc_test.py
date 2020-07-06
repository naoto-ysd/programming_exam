# カレンダーモジュールをインポート
import calendar

print('年を入力してください')
# month関数の引数は数値である必要があるため、標準入力からの値はint関数で数値にしておく
year = int(input())

print('月を入力してください')
# month関数の引数は数値である必要があるため、標準入力からの値はint関数で数値にしておく
month = int(input())

# カレンダーを出力
print(calendar.month(year, month))