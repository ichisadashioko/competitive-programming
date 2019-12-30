import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        String opinions = sc.nextLine();
        StringTokenizer st = new StringTokenizer(opinions);

        for (int i = 0; i < n; i++) {
            String o = st.nextToken();

            if (Integer.parseInt(o) == 1) {
                System.out.println("HARD");
                return;
            }
        }
        System.out.println("EASY");
        sc.close();
    }
}