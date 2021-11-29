import java.math.BigInteger;
import java.util.Scanner;

public class Main {

    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        
        int n = sc.nextInt();
        
        BigInteger ans = BigInteger.valueOf(36).pow(n - 1);
        ans = ans.multiply(BigInteger.valueOf(n));
        ans = ans.multiply(BigInteger.valueOf(26));
        ans = ans.add(BigInteger.valueOf(36).pow(n));

        System.out.println(ans);
    }
}