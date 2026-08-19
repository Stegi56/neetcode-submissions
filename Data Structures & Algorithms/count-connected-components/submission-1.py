class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        nodes = defaultdict(list)
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])

        visited = set()
        nodeCounter = 0
        def dfs(prev, cur):
            nonlocal nodeCounter
            if cur in visited:
                return
            
            visited.add(cur)
            nodeCounter += 1
            for n in nodes[cur]:
                if n != prev:
                    dfs(cur, n)
            return

        counter = 0
        keys = set(nodes.keys())
        while visited != keys:
            dfs(float("-inf"), next(iter(keys - visited)))
            counter += 1
        
        return counter + (n - nodeCounter)
