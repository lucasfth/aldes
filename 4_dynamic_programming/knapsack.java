import java.util.PriorityQueue;
import java.util.Scanner;

public class knapsack {
  static Scanner sc;
    public static void main(String[] args) {
      sc = new Scanner(System.in);
      while(sc.hasNextInt()) {
        // long sTime = System.currentTimeMillis();
        int W = sc.nextInt();
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
          values[i] = sc.nextInt();
          weights[i] = sc.nextInt();
        }
        solve(n, W, values, weights);
        // System.out.println("--- Time: " + (System.currentTimeMillis() - sTime) + "ms ---");
      }
      sc.close();
    }

    static void solve(int n, int W, int[] values, int[] weights) {
      // First row is automatically 0
      int[][] M = new int[n+1][W+1];

      for (int i = 1; i < n+1; i++) {
        for (int w = 0; w < W+1; w++) {
          int weight = weights[i-1];
          if (weight > w) {
            M[i][w] = M[i-1][w];
            continue;
          }
          M[i][w] = Math.max(M[i-1][w], values[i-1] + M[i-1][w-weight]);
        }
      }

      int w = W;
      PriorityQueue<Integer> pq = new PriorityQueue<>(n);
      for (int i = n; i > 0; i--) {
          if (M[i][w] != M[i-1][w]) {  
              pq.add(i-1);
              w -= weights[i-1];
          }
      }

      StringBuilder output = new StringBuilder();
      output.append(pq.size()).append("\n");

      while (!pq.isEmpty()) {
        output.append(pq.poll()).append((pq.isEmpty() ? "\n" : " "));
      }
      System.out.print(output.toString());
    }
}
