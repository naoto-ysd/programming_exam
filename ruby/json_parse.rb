require 'json'
require "csv"

direcrtory = Dir.home + "/Downloads/posts2"

Dir.foreach(direcrtory) do |item|
  next if item == '.' or item == '..'
  File.open(direcrtory + "/" + item) do |f|
    data = JSON.load(f)
    CSV.open(Dir.home + "/Desktop/posts.csv","a") do |csv|
      csv << [data['post']['number'],data['post']['name'],data['post']['category'],data['post']['created_by']['name'],data['post']['updated_by']['name']]
    end
  end
end

