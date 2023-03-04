directory = ARGV[0]
results_file = ARGV[1]
error_file = ARGV[2]

# now()、current_date、current_timestamp、current_timeでgrep
error = File.open(error_file, 'w')
File.open(results_file, 'w') do |frf|
  Dir.glob("#{directory}/**/*").select { |f| File.file?(f) && (f.include?('db/') || f.include?('lib/') || f.include?('app/')) && !f.include?('images/') && !f.include?('img/') && !f.include?('rspec/') && !f.include?('.pdf') }.each do |file|
    File.foreach(file) do |line|
      begin
        if line.match(/[nN][oO][wW]\(\)/) \
            || line.match(/[cC][uU][rR][rR][eE][nN][tT]_[dD][aA][tT][eE]/) \
            || line.match(/[cC][uU][rR][rR][eE][nN][tT]_[tT][iI][mM][eE][sS][tT][aA][mM][pP]/) \
            || line.match(/[cC][uU][rR][rR][eE][nN][tT]_[tT][iI][mM][eE]/)
          frf << file + "\n"
        end
      rescue
        error << file + "\n"
      end
    end
  end
end


