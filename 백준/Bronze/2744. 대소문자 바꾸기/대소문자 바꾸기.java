import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		String result = "";
		for(char x : str.toCharArray()) {
        
			if(Character.isLowerCase(x)) {
				result += Character.toUpperCase(x);
			} else {
				result += Character.toLowerCase(x);
			}
            
		}
		System.out.println(result);
	}
}