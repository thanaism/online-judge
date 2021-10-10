n, *s = *$<
n = n.to_i
c = "MARCH".chars
l = []
5.times do |i|
  l << s.map { |x| x[0] == c[i] ? 1 : 0 }.sum
end

ans = 0
(1 << 5).times do |i|
  buf = 1
  cnt = 0
  5.times do |j|
    if i >> j & 1 == 1
      cnt += 1
      buf *= l[j]
    end
  end
  ans += buf if cnt == 3
end

puts ans
