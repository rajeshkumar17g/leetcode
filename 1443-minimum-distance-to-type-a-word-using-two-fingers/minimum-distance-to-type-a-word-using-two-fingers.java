class Solution {
    public int minimumDistance(String word) {
        int n = word.length();
        if(n < 3) return 0;
        
        char[] arr = word.toCharArray();
        int[] store = new int[27];
        for(int i=0; i<27; ++i) store[i] = Integer.MAX_VALUE;
        
        store[26] = dist(arr[1], arr[0]);
        store[arr[0]-'A'] = 0;
        for(int k=2; k<n; ++k) {
            int delta = dist(arr[k], arr[k-1]), min = store[26];
            for(int i=0; i<27; ++i) {
                if(store[i] < min) min = Math.min(min, store[i] + dist(arr[k], (char) (i + 'A')));
                if(store[i] < Integer.MAX_VALUE) store[i] += delta;
            }
            store[arr[k-1]-'A'] = Math.min(store[arr[k-1]-'A'], min);
        }
        
        int ans = Integer.MAX_VALUE;
        for(int x: store) ans = Math.min(ans, x);
        
        return ans;
    }
    
    private int dist(char a, char b) {
        int i = a - 'A', j = b - 'A';
        return Math.abs(i/6 - j/6) + Math.abs(i%6 - j%6);
    }
}