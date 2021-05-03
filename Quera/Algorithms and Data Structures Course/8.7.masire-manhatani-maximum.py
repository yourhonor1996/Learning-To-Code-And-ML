n,m = [int(item) for item in input().split()]
nums = []
for i in range(n):
    nums.append([int(item) for item in input().split()])
    
dp = [[None for j in range(m)] for i in range(n)]
parent = [[None for j in range(m)] for i in range(n)]

dp[n-1][1] = nums[n-1][1]

for i in range(n):
    for j in range(m-1, -1, -1):
        if (dp[i+1][j] > dp[i][j]):
            dp[i][j] = dp[i+1][j] + nums[i][j]
            parent[i][j] = 0 #down
        else:
            dp[i][j] = dp[i][j-1] + nums[i][j]
            parent[i][j] = 1 #left     
        
current_row = 0
current_column = m-1
path = []
while([current_row, current_column] != [n-1, 0]):
    if (parent[current_row][current_column] == 0):
        path.append('U')
    else:
        path.append('R')
        



