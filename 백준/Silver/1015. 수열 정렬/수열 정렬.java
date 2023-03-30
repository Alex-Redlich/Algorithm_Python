import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
/**
 * 백준 전체 1015 문제 알고리즘 클래스
 *
 * @author RWB
 * @see <a href="https://blog.itcode.dev/posts/2021/06/22/a1015">1015 풀이</a>
 * @since 2021.06.22 Tue 01:23:31
 */
public class Main
{
    /**
     * 메인 함수
     *
     * @param args: [String[]] 매개변수
     *
     * @throws IOException 데이터 입출력 예외
     */
    public static void main(String[] args) throws IOException
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        // 배열의 크기
        int N = Integer.parseInt(reader.readLine());
        
        // 원본 배열
        int[][] A = new int[N][2];
        
        // 정렬 배열
        int[] B = new int[N];
        
        String[] temp = reader.readLine().split(" ");
        
        StringBuilder builder = new StringBuilder();
        
        for (int i = 0; i < N; i++)
        {
            A[i][0] = Integer.parseInt(temp[i]);
            A[i][1] = i;
        }
        
        // 정렬 수행
        sort(A);
        
        for (int i = 0; i < N; i++)
        {
            int index = A[i][1];
            
            B[index] = i;
        }
        
        for (int b : B)
        {
            builder.append(b).append(" ");
        }
        
        System.out.println(builder.toString().trim());
        
        writer.close();
        reader.close();
    }
    
    /**
     * 정렬 함수
     *
     * @param A: [int[][]] 대상 배열
     */
    private static void sort(int[][] A)
    {
        Arrays.sort(A, (next, current) ->
        {
            // 현재값이 더 클 경우
            if (next[0] < current[0])
            {
                return -1;
            }
            
            // 다음값이 더 클 경우
            else if (next[0] > current[0])
            {
                return 1;
            }
            
            // 현재값과 다음값이 같을 경우, 사전순 정렬
            else
            {
                return Integer.compare(next[1], current[1]);
            }
        });
    }
}