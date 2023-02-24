a = [-1,2,3,4,5]
b = (4..6).to_a

# puts a.inject(:+) + b.inject(:+)
# puts (a | b).inject(:-).abs + (a & b).inject(:+).abs
# puts (a | b).inject(:*).abs + b.inject(0) { |x,y| x + y ** 3}
# puts ((a || b).map(&:succ).inject(:*) * (a && b).inject(:*).abs2 + 29)

str = "liberty fish\r\n"
str.strip
p str
p "  abc  \r\n".strip 

count = 0
numbers = [3,40,39,29,10,50,59,69,70]
num = numbers.inject do |i,j|
  i > j ? i:j
end

p num