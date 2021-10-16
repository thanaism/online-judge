n = gets.to_i
$p = Array.new(n+1){[]}
(n-1).times{|i|
	b = gets.to_i
	$p[b] << i+2
}

def dfs(i)
	salaries = []
	return 1 if $p[i].length==0
	$p[i].each do |j|
		salaries << dfs(j)
	end
	min_salary = salaries.min
	max_salary = salaries.max
	max_salary + min_salary + 1
end

p dfs(1)