a,b,c = gets.split(" ").map(&:to_i)
puts b.between?(a+1,c-1) ? "Yes" : "No"