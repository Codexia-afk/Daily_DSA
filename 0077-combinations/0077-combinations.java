class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> path = new ArrayList<>();

        backtrack(1, n, k, path, ans);
        return ans;
    }

    private void backtrack(int start, int n, int k,
                           List<Integer> path,
                           List<List<Integer>> ans) {
        if (path.size() == k) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int num = start; num <= n; num++) {
            path.add(num);
            backtrack(num + 1, n, k, path, ans);
            path.remove(path.size() - 1);
        }
    }
}