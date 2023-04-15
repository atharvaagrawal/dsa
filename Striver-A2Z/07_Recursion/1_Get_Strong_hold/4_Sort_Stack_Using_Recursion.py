
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    # s.pop()
    # s.append()

    def sorted(self, s):
        
        # s = [2,4]  top =3
        def insert(s,top):
            # insert base case
            if len(s) == 0 or s[-1]<=top:
                s.append(top)
                return 

            val = s.pop()
            insert(s,top)
            s.append(val)
            

        def sort(s):
            if len(s) == 1:
                return
            
            top = s.pop()
            sort(s)
            insert(s,top)
        
        sort(s)


obj = Solution()
 
s = [11,2,32,3,41]
s = [3,2,1]

print("Before Sort:",s)
obj.sorted(s)
print("After Sort:",s)