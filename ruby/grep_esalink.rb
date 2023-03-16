# usage
# ruby grep.rb hoge fuga
def grep_esa_link(path,result_path)
  File.open(result_path,'w') do |result_csv|
    Dir.glob(File.join(path, '**/*.md')) do |filename|
      result = `grep -n "grep_word" "#{filename}"`
      result_csv.write("#{filename}: #{result}") unless result.empty?
    end
  end
end

path = ARGV[0]
result_path = ARGV[1]
grep_esa_link(path,result_path)