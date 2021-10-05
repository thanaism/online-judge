n = gets.to_i
a = gets.split(" ").map(&:to_i)
b = []
n.times do |i|
	b.push a[i] if i&1==0
	b.unshift a[i] if i&1==1
end

b.reverse! if n&1==1
puts b*" "