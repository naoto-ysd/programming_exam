require 'esa'
require 'uri'
require 'net/http'
require 'json'

client = Esa::Client.new(access_token: ENV['GET_ARTICLES'], current_team: ENV['ESA_TEAM'])
res = client.posts

uri = URI("https://api.esa.io/v1/teams/docs/posts?access_token=#{ENV['GET_ARTICLES']}")
res = Net::HTTP.get_response(uri)

File.open("posts.txt", mode = "w"){|f|
  f.write(res.body)  # ファイルに書き込む
}

