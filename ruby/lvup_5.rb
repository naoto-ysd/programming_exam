n = gets.chomp.to_i
arr = []
sum = 0

for i in 0...n do
  arr.push(gets.to_i)
end

arr.each do |j|
  if j >= 5
    sum += j
  end
end

p sum

# other answer
loop = gets.chomp.to_i
ans = 0

(1..loop).each do |i|
  num = gets.chomp.to_i

  ans = ans + num if num >= 5
end

puts ans
