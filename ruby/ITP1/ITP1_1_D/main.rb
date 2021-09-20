s = gets.to_i
h = s/3600
s %= 3600
m = s/60
s %= 60
puts "#{h}:#{m}:#{s}"