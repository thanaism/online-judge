n,m,k = gets.split(" ").map(&:to_i)
a = gets.split(" ").map{|e|e.to_i - 1}
$l = Array.new(n+1){[]}
(n-1).times do |i|
	x,y = gets.split(" ").map(&:to_i)
	x-=1;y-=1
	$l[x] << [y,i]
	$l[y] << [x,i]
end

$cnt = Array.new(n-1,0)
def dfs(from,to,pre)
	return true if from == to
	for ver,ind in $l[from]
		next if ver==pre
		if dfs(ver,to,from)
			$cnt[ind] += 1
			return true
		end
	end
	return false
end

for i in 1...m
	dfs(a[i-1],a[i],-1)
end

total = $cnt.sum
if (total+k)&1==1 || (total+k)<0
	p 0
	exit
end

MOD  = 998244353
dp = [0]*100001
dp[0] = 1
(n-1).times do |i|
	100000.downto($cnt[i]) do |j|
		dp[j] += dp[j-$cnt[i]]
		dp[j-$cnt[i]] %= MOD
	end
end

p dp[(total+k)>>1]


