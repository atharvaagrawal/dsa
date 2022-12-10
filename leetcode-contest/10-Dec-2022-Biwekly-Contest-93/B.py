class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:   
        max_sum = 0
        
        # Function to find the star sum for a given set of edges
        def star_sum(edges, vals):
            center = -1
            # Find the center node
            for edge in edges:
                if center == -1:
                    center = edge[0]
                else:
                    if edge[0] != center:
                        center = edge[1]
            # Sum the values of the center node and its neighbors
            sum = vals[center]
            for edge in edges:
                if edge[0] == center:
                    sum += vals[edge[1]]
                elif edge[1] == center:
                    sum += vals[edge[0]]
            return sum

        # Recursive function to find the maximum star sum
        def max_star_sum(edges, current_edges, k, max_sum):
            # If we have reached the maximum number of edges,
            # calculate the star sum for the current set of edges
            # and update the maximum sum if necessary
            if k == 0:
                sum = star_sum(current_edges, vals)
                max_sum = max(max_sum, sum)
                return max_sum
            # Try all possible edges that can be added to the current set
            for i in range(len(edges)):
                # Add the edge to the current set
                current_edges.append(edges[i])
                # Recursively call the function with one less edge left to add
                max_sum = max_star_sum(edges, current_edges, k - 1, max_sum)
                # Remove the edge from the current set
                current_edges.pop()
            return max_sum

        # Check if the graph has no edges
        if len(edges) == 0:
            return vals[0]
        # Check if the graph has any nodes with at least one neighbor
        has_neighbors = False
        for edge in edges:
            if edge[0] != edge[1]:
                has_neighbors = True
                break
        if not has_neighbors:
            return vals[0]
        # Find the maximum star sum using the max_star_sum function
        max_sum = max_star_sum(edges, [], k, 0)
        return max_sum
