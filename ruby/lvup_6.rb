array = [4, 0, 5, -1, 3, 10, 6, -8]
ans = 0
array.each do |arr|
  ans += arr if arr >= 5
end

puts ans

# other answer
array = [4, 0, 5, -1, 3, 10, 6, -8]
ans = 0

array.each { |element| ans += element if element >= 5 }

puts ans