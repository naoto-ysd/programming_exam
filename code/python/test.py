# 生徒の名前
students = ["A", "B", "C"]

# "80 70 90"と入力して、辞書にまとめて代入
scores = {}
for i, score in enumerate(input().split()):
    scores[students[i]] = score

# scoresの中には入力した点数が生徒の名前とセットで入っている
print(scores)