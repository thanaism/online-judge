n = gets.to_i
a = gets.split(" ").map(&:to_i)
h = Hash.new(0)
a.each{|i|h[i]+=1}
l = h.sort.reverse
ans=0
l.each do |k,_|
	if h[k]>1
		h[k] -= 2
		ans += k
		break
	end
end
l.each do |k,_|
	if h[k]>1
		ans *= k
		break
	end
end
puts ans