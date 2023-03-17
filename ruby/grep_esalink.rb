# usage
# ruby grep.rb hoge fuga
require 'csv'

def grep_esa_link(path,result_path)
  CSV.open(result_path,'wb') do |result_csv|
    Dir.glob(File.join(path, '**/*.md')) do |filename|
      File.foreach(filename).with_index do |line, line_num|
        if line.include?("grep_word")
          result_csv << [filename, line_num + 1, line.chomp!]
        end
      end
    end
  end
end

path = ARGV[0]
result_path = ARGV[1]
grep_esa_link(path,result_path)