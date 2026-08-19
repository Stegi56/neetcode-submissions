class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        nodes = defaultdict(list)
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        visited = set()
        def checkNoLoops(node, prev):
            if node in visited:
                return False

            visited.add(node)
            valid = True
            for leaf in nodes[node]:
                if leaf != prev:
                    valid = valid and checkNoLoops(leaf, node)
            return valid

        return (checkNoLoops(edges[0][0], None) and len(visited) == n)