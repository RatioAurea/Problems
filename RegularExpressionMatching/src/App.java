public class App {

    public static boolean ZeroChar(char[] c) {
        for (int i = 0; i < c.length; i++) {
            if (c[i] != '0') {
                return false;
            }
        }
        return true;
    }

    public static boolean DoMatch(String s1, String s2) {
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        int i = 0;
        int j = 0;
        while (i < c1.length && j < c2.length) {
            while (c1[i] == c2[j] || c2[j] == '.') {
                c1[i] = '0';
                c2[j] = '0'; 
                i++;
                j++;
            }
            if (c2[j] == '*') {
                int s = i - 1;
                while (c1[i] == c1[s]) {
                    c1[i] = '0';
                    i++;
                }
                c2[j] = '0';
                j++;
            }
            else {
                return false;
            }
        }
        if (ZeroChar(c1) && ZeroChar(c2)) {
            return true;
        }
        else {
            return false;
        }


    }

    public static void main(String[] args) throws Exception {
        String input1 = "aaaaabbcccd";
        String input2 = "a*bbc*.";

        boolean result = DoMatch(input1, input2);
        System.out.println(result);
    }
}
