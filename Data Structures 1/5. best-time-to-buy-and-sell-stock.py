class Solution:
    def maxProfitNaive(self, prices) -> int:
        n = len(prices)
        r = [0] * n
        
        for i in range(n):
            q = 0
            for j in range(i+1):
                if i == 0:
                    tmp = 0
                else:
                    tmp = r[i-1]
                q = max(prices[i] - prices[j], q, tmp)
            r[i] = q
        return r[n-1]


    def maxProfit(self, prices) -> int:
        # This solution uses a pivot pointer
        n = len(prices)
        # keep track of min left and max right
        min_left, max_right = [], []
        min_left_temp, max_right_temp = math.inf, -math.inf
        ans = 0
        for i in range(n):
            min_left_temp = min(min_left_temp, prices[i])
            min_left.append(min_left_temp)
            max_right_temp = max(max_right_temp, prices[n-i-1])
            max_right.append(max_right_temp)
        
        max_right = max_right[::-1]
        
        for i in range(n):
            ans = max(ans, max_right[i]-min_left[i])
            
        return(ans)

    def maxProfit(self, prices) -> int:
        n = len(prices)
        min_left_arr = []
        max_right_arr = []
        min_left = 10**5
        max_right = -1

        for i in range(n):
            # min on left of i (including i)
            min_left = min(min_left, prices[i])
            min_left_arr.append(min_left)
            # max on right of i (including i)
            max_right = max(max_right, prices[n - i - 1])
            max_right_arr.append(max_right)
                
        q = 0
        for i in range(n):
            q = max(q, max_right_arr[n - i - 1] - min_left_arr[i])
        return(q)