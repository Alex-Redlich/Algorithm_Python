import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scanner = new Scanner(System.in);
		String password;
		int x;
		
		x=scanner.nextInt();
		
		for(int i=0;i<x;i++)
		{
		
		password = scanner.next();
		
		if(password.length()>=6 && password.length()<=9)	
			System.out.println("yes");
		else 
			System.out.println("no");
		}
	}
}