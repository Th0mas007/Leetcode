class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges={(a,b) for a,b in connections}
        neighbors={city:[] for city in range(n)}
        visit=set()
        changes=0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        def dfs(city):
            nonlocal changes
            for nei in neighbors[city]:
                if nei in visit:
                    continue
                if (nei,city) not in edges:
                    changes+=1
                visit.add(nei)
                dfs(nei)
        visit.add(0)
        dfs(0)
        return changes