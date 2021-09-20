def insertionSort(a,n,g,count)
	(g...n).each {|i|
		v = a[i]
		j = i-g
		while j >= 0 && a[j] > v do
			a[j+g] = a[j]
			j = j-g
			count += 1
		end
		a[j+g] = v
	}
	return count,a
end

def shellSort(a, n)
	count = 0
	m = 1
	g = []
	while (3**m-1)/2 <= n do
		g.push((3**m-1)/2)
		m += 1
	end
	g.reverse!
	m-=1
	(0...m).each {|i|
		count,a = insertionSort(a,n,g[i],count)
	}
	puts m
	puts g.join(" ")
    puts count
	puts a
end

n = gets.to_i
l = []
n.times do
	l.push(gets.to_i)
end
shellSort(l,n)
