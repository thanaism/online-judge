n = gets.to_i
a = gets.split(" ").map(&:to_i)
count = 0
(0...n).each {|i|
	minj = i
	(i...n).each {|j|
		minj = j if a[j] < a[minj]
	}
	tmp = a[i]
	a[i] = a[minj]
	a[minj] = tmp
	count += 1 if i!=minj
}
puts a.join(" ")
puts count