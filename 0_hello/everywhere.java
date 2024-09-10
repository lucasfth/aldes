import java.util.HashSet;
import java.util.Scanner;

class Everywhere {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
  
    int testCases = sc.nextInt();
    
    for (int i = 0; i < testCases; i++) {
      int cities = sc.nextInt();
      sc.nextLine();
  
      HashSet<String> uniqueCities = new HashSet<>();

      for (int j = 0; j < cities; j++) {
        uniqueCities.add(sc.nextLine());
      }
      System.out.println(uniqueCities.size());
    }
  }
}
