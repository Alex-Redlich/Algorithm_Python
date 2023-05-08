import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        /* ah를 입력받아 h의 index위치를 알아낸다. 
        * 그다음 indexOf()메서드를 이용하여 누가 더 ah소리가 긴지 확인한다.   */
        Scanner sc = new Scanner(System.in);
        // ah 입력받기
        String mySound = sc.next();
        String docSound = sc.next();
        //h의 위치에 따라 갈지 말지 정하기
        if(mySound.indexOf("h")>= docSound.indexOf("h"))
            System.out.println("go");
        else
            System.out.println("no");
    }
}