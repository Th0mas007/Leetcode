class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colors=[None]*n
        for i in range(n):
            if colors[i] is None:
                colors[i]=1
                queue=[i]
                while queue:
                    currentNode=queue.pop(0)
                    for node in graph[currentNode]:
                        if colors[node] is None:
                            colors[node]=1-colors[currentNode]
                            queue.append(node)
                        elif colors[node]==colors[currentNode]:
                            return False
        return True
