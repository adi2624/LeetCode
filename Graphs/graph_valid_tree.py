class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if edges is None:
            return False
        # First lets create an adjacency map
        
        adjacency_list = dict()
        for i in range(n):
            adjacency_list[i] = set()
        
        for A,B in edges:
            adjacency_list[A].add(B)
            adjacency_list[B].add(A)
        
        seen = {0 : -1}
        stack = []
        stack.append(0)
        
        while len(stack) != 0:
            curr_element = stack.pop()
            for neighbors in adjacency_list[curr_element]:
                if neighbors == seen[curr_element]:
                    continue
                if neighbors in seen:
                    return False
                seen[neighbors] = curr_element
                stack.append(neighbors)
                
        return len(seen) == n
        