$val = 0

class Count
  def self.up
    $val = $val + 1
    $val == 3 ? true : false
  end
end

arr = [*1..10].select do
  Count.up
end

puts_method = puts arr
p_method = p arr
p puts_method.class
p p_method.class
p $val
