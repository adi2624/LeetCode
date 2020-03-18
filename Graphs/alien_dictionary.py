class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        return self.main_loop(words)
    
    def main_loop(self,words: List[str]) -> str:
        
        adjacency_list = dict()
        indegree = [0 for i in range(26)]
        self.buildGraph(words,indegree,adjacency_list)
        return self.topologicalSort(adjacency_list, indegree)
    
    def buildGraph(self,words,indegree,adjacency_list):
        
        # First we will populate all the characters of the given language into adjacency list
        
        for string in words:
            for char in string:
                if char not in adjacency_list:
                    adjacency_list[char] = set()
        
        # Now we will compare strings and see add graph edges according to diff chars
        
        for i in range(1,len(words)):
            first_word = words[i-1]
            second_word = words[i]
            
            min_len = min(len(first_word),len(second_word)) # we don't want out of bound idx
            
            for j in range(min_len):
                if first_word[j]!=second_word[j]:
                    
                    # Remember words are sorted lexicographically
                    
                    out_node = first_word[j]
                    in_node = second_word[j]
                    
                    if in_node not in adjacency_list[out_node]:
                        adjacency_list[out_node].add(in_node)
                        indegree[ord(in_node) - ord('a')] += 1
                    
                    break
                    
        
    def topologicalSort(self,adjacency_list,indegree):
        
        stack = []
        final_string = ""
        total_graph_nodes = len(adjacency_list.keys())
        
        for c in adjacency_list.keys():
            if indegree[ord(c) - ord('a')] == 0:
                stack.append(c)
        
        # Begin the Topological Sort
        
        while len(stack)!= 0:
            curr_element = stack.pop()
            final_string += curr_element
            incoming_edge_set = adjacency_list[curr_element]
            for in_char in incoming_edge_set:
                indegree[ord(in_char) - ord('a')] -= 1
                if indegree[ord(in_char) - ord('a')] == 0:
                    stack.append(in_char)

        return final_string if len(final_string) == total_graph_nodes else ""