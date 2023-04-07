import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

interface Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        long result = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).sum();

        System.out.println(result);
    }
}