# TLE SOLUTION
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         l = []

#         for i in range( len(temperatures) ):
#             j = i + 1
#             ct = 0
        
#             while j < len(temperatures):
#                 ct+=1
#                 if temperatures[j] > temperatures[i]:
#                     break            
#                 j+=1
        

#             if j == len(temperatures):
#                 if temperatures[j-1] <= temperatures[i]:
#                     ct = 0

#             l.append(ct)
#         return l

