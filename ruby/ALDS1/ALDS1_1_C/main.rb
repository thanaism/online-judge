require 'prime'
count = 0
gets.to_i.times do
	count += 1 if gets.to_i.prime?
end
puts count