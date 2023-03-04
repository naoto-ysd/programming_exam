require 'csv'

function_list = ARGV[0]
directory = ARGV[1]
results_file = ARGV[2]

File.open(results_file,"a") do |result|
  CSV.foreach(function_list) do |fl|
    # ファンクション名を1行ずつ読み込む
    fl.each do |grep_word|
      # ソースファイルを全てgrep
      Dir.glob("#{directory}/**/*").select { |f| File.file?(f) && !f.include?('log/') && !f.include?('coverage/') && !f.include?('spec/') && !f.include?('tmp/') && !f.include?('themes/') && !f.include?('vendor/') }.each do |file|
        # ファンクション名がヒットしたらファンクション名をテキストファイルに出力
        File.foreach(file) do |line|
          if line.include?(grep_word)
            # result << [file]
            result.write(grep_word + "\n")
          end
        end
      end
    end
  end
end
