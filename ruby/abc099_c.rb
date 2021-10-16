n = gets.to_i
dp = [1<<60]*(n+1)
dp[0] = 0
for i in 1..n
	dp[i] = [dp[i],dp[i-1]+1].min
	for j in 1..10
		k = i-6**j
		break if k<0
		dp[i] = [dp[i],dp[k]+1].min
	end
	for j in 1..10
		k = i-9**j
		break if k<0
		dp[i] = [dp[i],dp[k]+1].min
	end
end

p dp[n]