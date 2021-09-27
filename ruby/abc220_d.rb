n = gets.to_i
a = gets.split(" ").map(&:to_i)

MOD = 998244353

dp = Array.new(110000){Array.new(10,0)}
dp[1][a[0]] = 1

for i in 2..n
	for j in 0..9
		plus = (j+a[i-1])%10
		prod = (j*a[i-1])%10
		dp[i][plus] += dp[i-1][j]%MOD
		dp[i][plus] %= MOD
		dp[i][prod] += dp[i-1][j]%MOD
		dp[i][prod] %= MOD
	end
end

for i in 0..9
	puts dp[n][i]
end