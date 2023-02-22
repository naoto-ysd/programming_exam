# replace content in textfile
# usage
# ruby replace_txt.rb path
path = ARGV[0]

be_replaced_text = ENV['BE_REPLACED_TEXT']
replace_text = ENV['REPLACE_TEXT']

Dir.glob(File.join(path, '**/*.md')).each do |file|
  text = File.read(file)
  new_text = text.gsub(from, to)
  File.open(file, 'w') { |file| file.puts new_text }
end
