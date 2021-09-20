a,b = gets.split(" ").map(&:to_i)
op = a < b ? " < " : " > "
op = " == " if a == b
puts "a#{op}b"