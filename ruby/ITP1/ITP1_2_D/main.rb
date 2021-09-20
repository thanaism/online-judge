w,h,x,y,r = gets.split(" ").map(&:to_i)
ok = true
ok &= (x-r).between?(0,w)
ok &= (x+r).between?(0,w)
ok &= (y-r).between?(0,h)
ok &= (y+r).between?(0,h)
puts ok ? "Yes" : "No"