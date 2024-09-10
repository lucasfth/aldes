import java.util.Scanner;
import java.util.Arrays;

class Basic {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int length = sc.nextInt();
    int step = sc.nextInt();

    // SEVEN
    if (step == 1) {
      System.out.println("7");
    }

    sc.nextLine();
    int[] index = Arrays.stream(sc.nextLine().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();

    // BIGGER, SMALLER, EQUAL
    if (step == 2) {
      if (index[0] > index[1]) {
        System.out.println("Bigger");
      } else if (index[0] < index[1]) {
        System.out.println("Smaller");
      } else {
        System.out.println("Equal");
      }
    }

    // MEDIAN
    if (step == 3) {
      int[] sorted = {index[0], index[1], index[2]};
      Arrays.sort(sorted);
      System.out.println(sorted[1]);
    }

    // SUM
    if (step == 4) {
      System.out.println(Arrays.stream(index).sum());
    }

    // SUM OF EVEN
    if (step == 5) {
      System.out.println(Arrays.stream(index).filter(x -> x % 2 == 0).sum());
    }

    // TO STRING
    if (step == 6) {
      for (int i = 0; i < length; i++) {
        System.out.print((char) ('a' + index[i] % 26));
      }
      System.out.println("");
    }

    if (step == 7) {
      boolean[] visited = new boolean[length];
      int i = index[0];

      while (true) {
        if (visited[i]) {
          System.out.println("Cyclic");
          System.exit(0);
        }
        if (i - 1 > length) {
          System.out.println("Out");
          System.exit(0);
        }
        if (i - 1 == length) {
          System.out.println("Done");
          System.exit(0);
        }
        visited[i] = true;
        i = index[i];
      }
    }
  }
}
