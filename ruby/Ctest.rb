# 変数、引数 小文字のみ。スネークケースで書く(例: foo_)
# 関数,メソッド スネークケースで書く(例: foo_snake)。真偽値を返すメソッドであれば、最後に?をつける(例: foo_hoge?)
# 破壊的なメソッドはメソッドの最後に"!"をつける。(例: update!)
# 定数	大文字のみ、単語をアンダースコアで区切る。(例: MAX_SIZE).通常、モジュールレベル（関数の外側）に書く
# クラス (アッパーキャメルケースで書く 例: GetUser)
# ファイル名、ディレクトリ名。 スネークケースで書く(例: foo_class)
# 1文字変数は使わない。iとかoは1と0で間違ったりするから

count = gets.chomp.to_i
sum = 0

(1..count).each do |i|
  line = gets.chomp.split(' ')
  if line[0].to_i == line[1].to_i
    sum += line[0].to_i * line[1].to_i
  else
    sum += line[0].to_i + line[1].to_i
  end
end

puts sum
