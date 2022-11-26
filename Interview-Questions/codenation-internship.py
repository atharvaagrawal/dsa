class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        x,y,z= 0,0,0
        count = 0
        
        for i in range(len(B)):
            # Query 1
            x = B[i][0]
            y = B[i][1]
            z = B[i][2]
            print("Xup:",x,y,B[i][2])
                
            for j in range(abs(x-y)):
                print("X:",x,y,z)
                print("A:",A)
                print("j:",j)            
                if len(A) >= x+y and len(A) > x+j and A[x+j-1] != 0:
                    print("len(A):",len(A),"X+y:",x+j,"Yth Bit:",A[x+j-1])
                    print(A[x-1+j],z) 
                    print("A[x-1+j] ^ z:",A[x-1+j] ^ z )
                    A[x-1+j] = A[x-1+j] ^ z 
                    count +=1
                print()
            z = 0
            print("\n\n")
        return count

s = Solution()

# A = [2,4,3,5,4]
# B = [[3,1,4],[2,3,7]] #3

# A = [1,4]
# B = [[2,1,3]]  # 0

A = [26,43,16,18,34,17,19,25,28,26,10,36,33]
B = [[3,4,50],
[5,4,28],
[13,1,13],
[8,3,36],
[10,3,45],
[2,3,23],
[5,2,43]]    #2

print(s.solve(A,B))