n = gets.to_i
INF = 1<<60
d = Hash.new(0)
s = gets.chomp
s.each_char do |c|
	d[c] += 1
end
(n-1).times do
	s = gets.chomp
	h = Hash.new(0)
	s.each_char do |c|
		h[c] += 1
	end
	for key in 'a'..'z'
		d[key] = [d[key], h[key]].min
	end
end
ans = ""
for key in 'a'..'z'
	d[key].times do
		ans << key
	end
end
puts ans.chars.sort.join


