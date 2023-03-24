public class App {
    public static void main(String[] args) throws Exception {
        
        int[][] start = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};

        MyMatrix matrix = new MyMatrix(start);
        matrix.print();
        matrix.NextGeneration();
        matrix.print();
        matrix.NextGeneration();
        matrix.print();
    }
}
