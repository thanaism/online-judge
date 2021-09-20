n = gets.to_i
l = gets.split(" ").map(&:to_i)
puts [l.min,l.max,l.sum].join(" ")