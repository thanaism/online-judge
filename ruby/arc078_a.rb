n = gets.to_i
a = gets.split(" ").map(&:to_i)
total = a.sum
now = 0
ans = 1<<60
for i in 0..n-2
	now += a[i]
	ans = [ans,(total - 2 * now).abs].min
end
puts ans