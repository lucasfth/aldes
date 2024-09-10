import java.util.Scanner;
import java.util.Stack;

class Backspace {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    Stack<Character> stack = new Stack<>();

    char[] instance = sc.nextLine().toCharArray();

    for (char c : instance) {

      if (c != '<') {
        stack.add(c);
        continue;
      }
      
      if(stack.isEmpty()) {
        break;
      }

      stack.pop();
    }

    System.out.println(stack.toString().replaceAll("[\\[\\], ]", ""));
  }
}
