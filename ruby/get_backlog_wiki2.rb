require 'faraday'
require 'json'

BACKLOG_ENDPOINT = ENV['BACKLOG_ENDPOINT']
BACKLOG_API_KEY = ENV['BACKLOG_API_KEY']
BACKLOG_PROJECT_ID = ENV['BACKLOG_PROJECT_ID'].to_i

# Faradayクライアントの作成
conn = Faraday.new(url: "https://#{BACKLOG_ENDPOINT}") do |faraday|
  faraday.request :url_encoded
  faraday.adapter Faraday.default_adapter
  faraday.authorization :Bearer, BACKLOG_API_KEY
end

# プロジェクトIDを指定してWiki一覧を取得
path = "/api/v2/wikis?apiKey=#{BACKLOG_API_KEY}"

params = {
  projectIdOrKey: BACKLOG_PROJECT_ID,
  keyword: 'esa'
}

response = conn.get do |req|
  req.url path
  req.headers['Content-Type'] = 'application/x-www-form-urlencoded'
  req.body = params
end

# レスポンスのパース
wikis = JSON.parse(response.body)

# 取得したWiki一覧を出力
wikis.each do |wiki|
  puts "#{wiki['id']}: #{wiki['name']}"
end
