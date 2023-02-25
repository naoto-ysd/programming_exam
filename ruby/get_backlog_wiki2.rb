require 'faraday'
require 'net/http'
require 'uri'
require 'json'

BACKLOG_ENDPOINT = ENV['BACKLOG_ENDPOINT']
BACKLOG_API_KEY = ENV['BACKLOG_API_KEY']
BACKLOG_PROJECT_ID = ENV['BACKLOG_PROJECT_ID'].to_i

# API呼び出し用のメソッド
def call_api()
  url = URI.parse("https://#{BACKLOG_ENDPOINT}.backlog.jp/api/v2/wikis")
  req = Net::HTTP::Get.new(url)
  req['Content-Type'] = 'application/json'
  req['Authorization'] = BACKLOG_API_KEY
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER
  http.ca_file = '/etc/ssl/certs/ca-certificates.crt' # CA証明書のパスを指定
  p 'test'
  res = http.request(req)
  JSON.parse(res.body)
end

# Wikiページ一覧を取得する
wiki_pages = call_api
puts "Wikiページ一覧："
wiki_pages.each do |page|
  puts "#{page['name']} (#{page['id']})"
end


# path = "/api/v2/wikis?apiKey=#{BACKLOG_API_KEY}"

# connection = Faraday.new url: "https://#{BACKLOG_ENDPOINT}" do |faraday|
#   faraday.request  :url_encoded
#   faraday.adapter Faraday.default_adapter
# end

# p connection
# res = connection.get do |req|
#   req.url path
#   req.headers['Content-Type'] = 'application/x-www-form-urlencoded'
#   req.body = params
# end

# content_type = res['Content-Type']

# posts =  JSON.parse(res)
# p posts
