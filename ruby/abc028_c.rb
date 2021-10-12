l = gets.split(" ").map(&:to_i)
ans = []
(l.combination 3).each{|c|ans<<c.sum}
p ans.uniq.sort[-3]