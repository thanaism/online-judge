l = gets.split(?+)
p l.map{|s|s.include?('0')?0:1}.sum