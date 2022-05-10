# 変数、引数 小文字のみ。スネークケースで書く(例: foo_)
# 関数,メソッド スネークケースで書く(例: foo_snake)。真偽値を返すメソッドであれば、最後に?をつける(例: foo_hoge?)
# 破壊的なメソッドはメソッドの最後に"!"をつける。(例: update!)
# 定数	大文字のみ、単語をアンダースコアで区切る。(例: MAX_SIZE).通常、モジュールレベル（関数の外側）に書く
# クラス (アッパーキャメルケースで書く 例: GetUser)
# ファイル名、ディレクトリ名。 スネークケースで書く(例: foo_class)
# 1文字変数は使わない。iとかoは1と0で間違ったりするから

H,W = gets.split.map(&:to_i)
heights = Array.new(w)

for height_num in 0..h-1
  heights[height_num] = gets.chomp.chars
end

operation = gets.chomp.chars

operation.each do |op|
  for height_num in 0..h-1
    for width_num in 0..w
      if op == "D" && heights[width_num] == "#"
        if width_num == 0
          heights[width_num + 1] = "#"
        else
          heights[width_num + 1] = "#"
          heights[width_num - 1] = "#"
        end

        if height_num == 0
          heights[height_num+1][width_num + height_num + 1] = "#"
        else
          heights[height_num+1][width_num + height_num + 1] = "#"
          heights[height_num-1][width_num + height_num - 1] = "#"
        end

      elsif op == "E" && heights[width_num] == "."
        p heights
        if width_num == 0
          heights[width_num + 1] = "."
        else
          heights[width_num + 1] = "."
          heights[width_num - 1] = "."
        end

        if height_num == 0
          heights[height_num+1][width_num + height_num + 1] = "."
        else
          heights[height_num+1][width_num + height_num + 1] = "."
          heights[height_num-1][width_num + height_num - 1] = "."
        end
      end
    end
  end
end

heights.each do |height|
  height.each do |hi|
    print hi
  end
  print "\n"
end
