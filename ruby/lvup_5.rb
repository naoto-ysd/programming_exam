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
