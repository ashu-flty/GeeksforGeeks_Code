#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        s=0
        for i in range(K):
            s+=GeekNum[i]
        j=0
        for i in range(N-K):
            GeekNum.append(s)
            s=s-GeekNum[j]+GeekNum[-1]
            j+=1
        return GeekNum[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends