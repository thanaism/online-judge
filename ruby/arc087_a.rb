n = gets.to_i
a = gets.split(" ").map(&:to_i)
h = Hash.new(0)
a.each{|i|h[i]+=1}
p h.keys.map{|k|d=h[k]-k;d>=0?d:h[k]}.sum