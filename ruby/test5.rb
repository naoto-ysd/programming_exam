require "pry"

class Student
  
  def avg(english: , math:)
    binding.pry
    avg = (english + math) / 2
  end

end

ENGLISH = 60
MATH = 80

student = Student.new
pp student.avg(english: ENGLISH, math: MATH)