class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int m = heights.length, n = heights[0].length;

        // 第一列和第一行的格子一定可以流入太平洋
        // 加入队列，同时标记为已访问
        boolean[][] visitedP = new boolean[m][n];
        Queue<int[]> queueP = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            queueP.offer(new int[]{i, 0});
            visitedP[i][0] = true;
        }
        for (int j = 1; j < n; j++) {
            queueP.offer(new int[]{0, j});
            visitedP[0][j] = true;
        }
        // 进行 BFS 搜索，找出所有可以流入太平洋的格子
        bfs(heights, queueP, visitedP);

        // 最后一列和最后一行的格子一定可以流入大西洋
        // 加入队列，同时标记为已访问
        boolean[][] visitedA = new boolean[m][n];
        Queue<int[]> queueA = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            queueA.offer(new int[]{i, n - 1});
            visitedA[i][n - 1] = true;
        }
        for (int j = 0; j < n - 1; j++) {
            queueA.offer(new int[]{m - 1, j});
            visitedA[m - 1][j] = true;
        }
        // 进行 BFS 搜索，找出所有可以流入大西洋的格子
        bfs(heights, queueA, visitedA);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visitedP[i][j] && visitedA[i][j]) {
                    // 筛选出既可以流入太平洋又可以流入大西洋的格子
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        return res;
    }

    void bfs(int[][] heights, Queue<int[]> queue, boolean[][] visited) {
        int m = heights.length, n = heights[0].length;
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // BFS 算法框架
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int[] dir : dirs) {
                int x = cur[0] + dir[0], y = cur[1] + dir[1];
                if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y]
                        || heights[x][y] < heights[cur[0]][cur[1]]) {
                    continue;
                }
                queue.offer(new int[]{x, y});
                visited[x][y] = true;
            }
        }
    }
}//om*n,om*n