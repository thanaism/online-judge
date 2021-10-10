n,m = gets.split(" ").map(&:to_i)

total = (n-m)*100 + m*1900
p total*(1<<m)