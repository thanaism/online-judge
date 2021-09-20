a,b,c = gets.split(" ").map(&:to_i)
ans = 0
(a..b).each do |i|
	ans += 1 if c%i == 0
end
puts ans