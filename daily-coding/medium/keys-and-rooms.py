# https://leetcode.com/problems/keys-and-rooms/description/ 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:    
        visited = [0 for i in range(len(rooms))]
        
        s = set(rooms[0])
        visited[0] = 1
        for _ in range(len(rooms)):
            keys = list(s)
            
            for key in keys:
                if visited[key] == 0:
                    visited[key] = 1
                    
                    for i in rooms[key]:        
                        s.add(i)

        s = set(visited)

        if len(s) >= 2:
            return False
        return True 

