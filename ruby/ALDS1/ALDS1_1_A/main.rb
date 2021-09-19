n = gets.to_i
a = gets.split(" ").map(&:to_i)
for i in 1...n
	puts [a[0,i].sort, a[i,n-i]].join(" ")
end
puts a.sort.join(" ")