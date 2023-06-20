import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		//짝수 여부는 (짝수여부 궁금한 수) % 2 == 0을 하면 된다.
		//그리고 당연한거지만 두 수의 합이 차보다 커야하니깐 A가 B보다 작으면 안된다는 조건도 넣어준다.
		if((A + B) % 2 != 0 || A < B) {
			System.out.println(-1);
		}else {
			//두 수를 공백을 두고 출력하라 했으니 식 사이에 공백을 넣어준다.
			System.out.println(((A + B) / 2) + " " + (((A + B) / 2) - B));
		}
	}

}