public class MyMatrix {

    int i;
    int j;
    int[][] myMatrix;

    public MyMatrix(int[][] matrix) {
        this.i = matrix.length;
        this.j = matrix[0].length;
        this.myMatrix = matrix;
    }

    private int NeighboorOnes(int i, int j){
        int onesNo = 0;
        int[][] neighboors = {{i - 1 , j - 1}, {i - 1, j}, {i - 1, j + 1}, {i, j - 1}, {i, j + 1}, {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}};
        for (int[] pair : neighboors) {
            try {
                if (myMatrix[pair[0]][pair[1]] == 1) {
                    onesNo++;
                }
            } catch (Exception e) {
                
            }
        }
        return onesNo;
    }

    public void NextGeneration() {
        int[][] newGeneration = new int[i][j];
        for (int p = 0; p < i; p++) {
            for (int q = 0; q < j; q++) {
                if (myMatrix[p][q] == 1 && NeighboorOnes(p, q) < 2) {
                    newGeneration[p][q] = 0;
                }
                else if (myMatrix[p][q] == 1 && (NeighboorOnes(p, q) == 2 || NeighboorOnes(p, q) == 3)) {
                    newGeneration[p][q] = 1;
                }
                else if (myMatrix[p][q] == 1 && NeighboorOnes(p, q) > 3) {
                    newGeneration[p][q] = 0;
                }
                else if (myMatrix[p][q] == 0 && NeighboorOnes(p, q) == 3) {
                    newGeneration[p][q] = 1;
                }
                else {
                    newGeneration[p][q] = 0;
                }
            }
        }
        this.myMatrix = newGeneration;
    }

    public void print() {
        for (int[] row : myMatrix) {
            StringBuffer string = new StringBuffer();
            for (int k : row) {
                string.append(String.valueOf(k));
                string.append(" ");
            }
            System.out.println(string.toString());
        }
        System.out.println();
    }
}