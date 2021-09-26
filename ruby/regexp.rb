def replace!(text, key, new_text)
	regexp = Regexp.new('\{# *' << key << ' *#\}')
	p regexp
	text.gsub!(regexp, new_text.to_s)
	text
end

text = 'abcdef'
company = '2ndcommunity'
replace!(text, 'company_name', company)