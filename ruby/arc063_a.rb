s = gets.chomp
cnt = 0
pre = s[0]
s.each_char do |c|
	if c != pre
		cnt += 1
	end
	pre = c
end
puts cnt