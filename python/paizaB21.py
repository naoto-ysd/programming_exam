N = int(input())

arr = []
fukusu = ""


for n in range(N):
  # 単語の入力
  tango = input()

  # 単語に複数形が含まれるか検索
  if len(tango) - tango.rfind("s") == 1 or len(tango) - tango.rfind("sh") == 2 or len(tango) - tango.rfind("ch") == 2 or len(tango) - tango.rfind("o") == 1 or len(tango) - tango.rfind("x") == 1:
    tango = tango + "es"
  elif len(tango) - tango.rfind("f") == 1:
    # 単語末尾のfをとる
    tango = tango.rstrip("f") + "ves"
    tango

  elif len(tango) - tango.rfind("fe") == 2:
    # 単語の末尾のfeをとる
    tango = tango.rstrip("fe") + "ves"

    

  # 配列に複数形に変換した単語を入れる
  arr.append(tango)

# 配列の出力
for item in arr:
  print(item)
