import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n == 0) {  //0 일때 영문명 출력
            System.out.print("YONSEI");
        } else {  //N = 1일때 슬로건 출력
            System.out.print("Leading the Way to the Future");
        }
    }
}