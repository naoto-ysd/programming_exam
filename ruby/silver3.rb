a = [-1, 2, 3, 4, 5]
b = (4..6).to_a

puts (a | b).inject(:-).abs + (a & b).inject(:+).abs

puts (a | b).inject(:*) + b.inject(0) { |x, y| x + y ** 3 }

puts ((a || b).map(&:succ).inject(:*) * (a && b).inject(:*).abs2 + 29)

puts (a || b).map(&:succ)