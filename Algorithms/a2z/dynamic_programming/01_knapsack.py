def knapsack(W,wt,val,N):
    
    def solve(n,capacity):
        # memoization for dynamic programming.
        dp = {}

        # If items or capacity is 0, result would also be zero.
        if n ==0 or capacity == 0:
            return 0
        
        # If requirement is present in memoization
        elif (n,capacity) in dp:
            return dp[(n,capacity)]
        else:
            current_weight = wt[n-1]
            current_value = val[n-1]

            if current_weight <= capacity:
                # If item is selected
                c1 = capacity - solve(n-1,capacity)

                # If item is not selected
                c2 = solve(n-1,capacity)

                # selecting best choice , i.e. maximum benefit from choices. 
                c = max(c1,c2)
            else:
                # check till you find item is under or equal 
                c =  solve(n-1,capacity)
            
            dp[(n,capacity)] = c
            return c
    
    solve(N,W)