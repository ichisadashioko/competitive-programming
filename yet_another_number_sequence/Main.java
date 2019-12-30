import java.util.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        StringTokenizer st = new StringTokenizer(input);

        int n = Integer.parseInt(st.nextToken());
        n++;
        int k = Integer.parseInt(st.nextToken());

        int limit = (int) Math.pow(10, 9);

        int fib_a = 1;
        int fib_b = 1;

        int sum = 0;

        for (int i = 1; i < n; i++) {
            int Ai = fib_b * (int) Math.pow(i, k);
            sum += (Ai % limit);

            fib_b += fib_a;
            fib_a = fib_b - fib_a;
        }

        System.out.println(sum);

        sc.close();

    }
}