h = Hash.new("default value")

h[:a]
h[:b] = 100

p h

p String.method_defined?(:to_a)
