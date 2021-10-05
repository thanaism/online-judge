n, _ = gets.split(" ").map(&:to_i)
d = gets.split(" ").map(&:to_i)
ok=[]
for i in 0..9
	ok << i if !d.include?(i)
end


s = n.to_s
bigger = false
ans = String.new


s.each_char do |c|
	i = c.to_i
	if !bigger
		m = -1
		ok.each do |j|
			if m != -1
				next
			elsif j>i
				bigger = true
				m = j
			elsif j==i
				m = j
			end
		end
	else
		m = ok[0]
	end
	ans << m.to_s
end

if ans.to_i<n
	ans = String.new
	n.to_s.length.times do
		ans << ok[0].to_s
	end
	ans = (ok[0]!=0 ? ok[0].to_s : ok[1].to_s) << ans
end
puts ans