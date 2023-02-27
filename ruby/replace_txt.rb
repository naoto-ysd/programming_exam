# usage
# ruby replace_txt.rb ~/directory name
# replace content in textfile

def replace_attached_files(path)
  from = ENV['FROM_URL']
  to = ENV['TO_URL']
  Dir.foreach(path) do |filename|
    next unless filename.end_with?('.md')
    Dir.glob(File.join(path, '**/*.md')).each do |file|
      text = File.read(file)
      new_text = text.gsub(from, to)
      File.open(file, 'w') { |file| file.puts new_text }
    end
  end
end

def replace_atag(path)
  Dir.foreach(path) do |filename|
    next unless filename.end_with?('.md')
    # aタグの置換
    Dir.glob(File.join(path, '**/*.md')).each do |file|
      content = File.read(file)
      replaced_content = content.gsub(/<a href="(.+?)">(.+?)<\/a>/, '[\2](\1)')
      #  target="_blank"を消す
      replaced_content = replaced_content.gsub(/" target="_blank/,'')
      File.write(file, replaced_content)
    end
  end
end

def replace_imgtag(path)
  from_attachment_file = ENV['FROM_ATTACHMENT']
  to_attachment_file = ENV['TO_ATTACHMENT']
  Dir.foreach(path) do |file|
    next unless file.end_with?('.md')
    Dir.glob(File.join(path, '**/*.md')).each do |file|
      # imgタグの置換
      lines = File.readlines(file)
      new_lines = []
    
      lines.each do |line|
        # 正規表現でimgタグを抽出する
        match = /<img .*?src="([^"]+)".*?>/.match(line)
    
        if match
          # URLを抜き出して変換する
          url = match[1]
          # URLはbacklog用のものに変換
          url = url.gsub(from_attachment_file,to_attachment_file)
          new_line = "![Alt text](#{url})"
          new_lines << new_line
        else
          new_lines << line
        end
      end
    
      # 置換後の行を上書き保存する
      File.write(file, new_lines.join(''))
    end
  end
end

path = ARGV[0]
replace_attached_files(path)
replace_atag(path)
replace_imgtag(path)
