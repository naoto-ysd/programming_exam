# 変数、引数 小文字のみ。スネークケースで書く(例: foo_)
# 関数,メソッド スネークケースで書く(例: foo_snake)。真偽値を返すメソッドであれば、最後に?をつける(例: foo_hoge?)
# 破壊的なメソッドはメソッドの最後に"!"をつける。(例: update!)
# 定数	大文字のみ、単語をアンダースコアで区切る。(例: MAX_SIZE).通常、モジュールレベル（関数の外側）に書く
# クラス (アッパーキャメルケースで書く 例: GetUser)
# ファイル名、ディレクトリ名。 スネークケースで書く(例: foo_class)
# 1文字変数は使わない。iとかoは1と0で間違ったりするから
h,w,n = gets.split.map(&:to_i)

heights = []
operation = Array.new(n)
temp_width = Array.new(w)

for height_num in 0..h-1
  temp_width[height_num] = gets.split.map(&:to_s)
end

temp_width.each do |tw|
  heights.push(tw)
end

operation.push(gets.to_s)

operation.each do |op|
  for height_num in 0..h-1
    for width_num in 0..w
      if op == 'D' && heights[width_num] == '#'
        heights[width_num + 1] = '#'
        heights[width_num - 1] = '#'
        heights[height_num - 1] = '#'
      elsif op == 'E'

      end
    end
  end
end

heights.each do |height|
  p height
end

# print "hello\n"
