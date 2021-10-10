n, k = gets.split(" ").map(&:to_i)
a = gets.split(" ").map(&:to_i)

d = Hash.new(0)
a.each { |i| d[i] += 1 }

l = d.size
d = d.sort_by { |_, v| v }

ans = 0
l.times { |i|
  break if l - i <= k
  ans += d[i][1]
}

puts ans
