n = gets.chomp.to_i
x = 0
y = 0
ans = 0
(1..n).each do |i|
  input = gets.chomp.split(' ')
  if input[0] == input[1]
    ans += input[0].to_i * input[1].to_i
  else
    ans += input[0].to_i + input[1].to_i
  end
end

p ans

# other answers
count = gets.chomp.to_i
sum = 0

(1..count).each do |i|
  line = gets.chomp.split(' ')
  if line[0].to_i == line[1].to_i
    sum += line[0].to_i * line[1].to_i
  else
    sum += line[0].to_i + line[1].to_i
  end
end

puts sum
