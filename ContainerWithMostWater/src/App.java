public class App {
    public static void main(String[] args) throws Exception {
        int[] heights = {6, 1, 2, 20, 3, 9, 2, 6, 18, 2, 4, 8};
        int start = 0;
        int end = heights.length - 1;
        int maxVolume = 0;
        while (start != end) {
            int currentVolume = (end - start) * Math.min(heights[start], heights[end]);
            if (currentVolume > maxVolume) {
                maxVolume = currentVolume;
            }

            if (heights[start] < heights[end]) {
                start++;    
            }
            else {
                end--;
            }
        }
        System.out.println(maxVolume);
    }
}
