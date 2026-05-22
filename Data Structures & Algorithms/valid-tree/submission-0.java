class Solution {

    private Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

    public boolean validTree(int n, int[][] edges) {
        adjacencyList.clear();  
    
        if (n == 1) return edges.length == 0;
    
        if (edges.length == 0) return false;
    
        for (int[] edge : edges) {
            int node1 = edge[0];
            int node2 = edge[1];
            adjacencyList.putIfAbsent(node1, new ArrayList<>());
            adjacencyList.putIfAbsent(node2, new ArrayList<>());
            adjacencyList.get(node1).add(node2);
            adjacencyList.get(node2).add(node1);
        }
    
        Set<Integer> visited = new HashSet<>();
    
        if (!depthFirstSearch(edges[0][0], -1, visited)) return false;
    
        return visited.size() == n;
    }

    private boolean depthFirstSearch(int node, int previous, Set<Integer> visited) {
        if (visited.contains(node)) return false;

        visited.add(node);

        for (int neighbor : adjacencyList.get(node)) {
            if (neighbor == previous) continue;

            if (!depthFirstSearch(neighbor, node, visited)) return false;
        }

        return true;
    }
}
//on,on