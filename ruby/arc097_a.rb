s = gets.chomp
k = gets.to_i
n = s.length
d = []
for i in 0...n
	for j in i+1..[n,i+1+k].min
		d << s[i...j]
	end
end

puts d.uniq.sort[k-1]