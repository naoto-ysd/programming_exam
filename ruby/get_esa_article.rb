require 'uri'
require 'net/http'
client = Esa::Client.new(access_token: ENV['GET_ARTICLES'], current_team: ENV['ESA_TEAM'])
p client.user
# /v1/teams/docs/posts

# uri = URI('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
# res = Net::HTTP.get_response(uri)
# puts res.body if res.is_a?(Net::HTTPSuccess)