denominations = eval(raw_input('denominations:'))
amount = eval(raw_input('amount:'))
l = len(denominations)
result_table = [[0 for i in range(l)] for j in range(amount+1)]
for x in range(l):
    result_table[0][x] = 1
for i in range(1,amount+1):
    for j in range(l):
            x = result_table[i - denominations[j]][j] if i-denominations[j] >= 0 else 0
            y = result_table[i][j-1] if j >= 1 else 0
            result_table[i][j]=x+y
        
            
print 'number of possible ways:',result_table[amount][l-1]
