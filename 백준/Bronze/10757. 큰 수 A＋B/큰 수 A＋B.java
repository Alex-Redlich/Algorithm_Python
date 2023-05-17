import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		String str_A = in.next();
		String str_B = in.next();
		
		// 두 개의 수 중 가장 긴 자리수 길이를 구해둠
		int max_length = Math.max(str_A.length(), str_B.length());
		
		
		int[] A = new int[max_length + 1];	// 마지막 자리수 올림이 있을 수 있으므로 +1
		int[] B = new int[max_length + 1];	// 마지막 자리수 올림이 있을 수 있으므로 +1
		
		
 
		// A 초기화
		for(int i = str_A.length() - 1, idx = 0; i >= 0; i--, idx++) {
			A[idx] = str_A.charAt(i) - '0';	// 맨 뒤 문자부터 역순으로 하나씩 저장
		}
 
		
		// B 초기화
		for(int i = str_B.length() - 1, idx = 0; i >= 0; i--, idx++) {
			B[idx] = str_B.charAt(i) - '0';	// 맨 뒤 문자부터 역순으로 하나씩 저장
		}
		
		// 덧셈
		for(int i = 0; i < max_length; i++) {
			int value = A[i] + B[i];
			A[i] = value % 10;		// 더한 값의 10으로 나눈 나머지가 자리값이 됨
			A[i + 1] += (value / 10);	// 더한 값의 10으로 나눈 몫이 올림값이 됨
		}
		
		// A배열 역순 출력
		// 가장 높은 자리수가 0일 수도 있기 때문에 0이 아닐 경우에만 출력
		StringBuilder sb = new StringBuilder();
		if(A[max_length] != 0) {
			sb.append(A[max_length]);
		}
		for(int i = max_length - 1; i >= 0; i--) {
			sb.append(A[i]);
		}
		
		System.out.println(sb);
	}
}