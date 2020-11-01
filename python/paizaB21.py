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

  elif len(tango) - tango.rfind("fe") == 2:
    # 単語の末尾のfeをとる
    tango = tango.rstrip("fe") + "ves"
  
  elif len(tango) - tango.rfind("y") == 1:
    matsubi2 = tango[len(tango)-2:len(tango)-1]
    if matsubi2 != "a" and matsubi2 != "i" and matsubi2 != "u" and matsubi2 != "e" and matsubi2 != "o":
      tango = tango[0:len(tango)-1] + "ies"
    else:
      tango = tango + "s"

  else:
    tango = tango + "s"

  # 配列に複数形に変換した単語を入れる
  arr.append(tango)
  

# 配列の出力
for item in arr:
  print(item)