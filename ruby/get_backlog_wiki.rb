require 'backlog_kit'

BACKLOG_SPACE_ID = ENV['BACKLOG_ENDPOINT']
BACKLOG_API_KEY = ENV['BACKLOG_API_KEY']
BACKLOG_PROJECT_ID = ENV['BACKLOG_PROJECT_ID'].to_i

client = BacklogKit::Client.new(
  space_id: BACKLOG_SPACE_ID,
  api_key: BACKLOG_API_KEY
)

space = client.get_space.body
p space
pages = client.get('wikis', projectIdOrKey: BACKLOG_PROJECT_ID).body
pages.each do | page |
  p page
end