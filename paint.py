
import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int Q = in.nextInt();
        int N = in.nextInt();
        int a=0;
        for (int i = 0; i < N; i++) {
            int X = in.nextInt();
            int Y = in.nextInt();
            int Z = in.nextInt();
            a=a+X*Y*Z;
        }
        a=a/5;
        if(Q>a)
        {
            System.out.print("true");
        }
        else
        {
            System.out.print("false");
        }
    }
}
