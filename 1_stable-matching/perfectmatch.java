import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

class Perfectmatch {
  public static HashMap<String, Boolean> pMatched;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int individuals = sc.nextInt();
    int nPref = sc.nextInt();
    
    sc.nextLine();
    
    HashMap<String, Stack<String>> proposers = new HashMap<>();
    pMatched = new HashMap<>();
    HashMap<String, HashMap<String, Integer>> rejecters = new HashMap<>();
    HashMap<String, String> match = new HashMap<>();
    
    // LOAD DATA IN
    // Load proposers
    for (int i = 0; i < individuals / 2; i++) {
      String[] tmp = sc.nextLine().split(" ");

      Stack<String> pref = new Stack<>();
      for (int j = tmp.length - 1; j > 0; j--) {
        pref.add(tmp[j]);
      }

      proposers.put(tmp[0], pref);
      pMatched.put(tmp[0], false);
    }
    // Load rejecters
    for (int i = 0; i < individuals / 2; i++) {
      String[] tmp = sc.nextLine().split(" ");

      HashMap<String, Integer> pref = new HashMap<>();
      for (int j = 1; j < tmp.length; j++) {
        pref.put(tmp[j], j);
      }

      rejecters.put(tmp[0], pref);
      match.put(tmp[0], "");
    }

    // FIND MATCHES
    while(true) {
      String unmatched = getUnmatched();

      // Print matches
      if (unmatched.equals("")) {
        for (String p : match.keySet()) {
          System.out.println(p + " " + match.get(p));
        }
        break;
      }

      // Propose to all
      for (int i = 0; i < nPref; i++) {
        String marryable = proposers.get(unmatched).pop();

        // Propose to unmatched
        if (match.get(marryable).equals("")) {
          match.put(marryable, unmatched);
          pMatched.put(unmatched, true);
          break;
        }

        String opponent = match.get(marryable);
        int oStatus = rejecters.get(marryable).get(opponent);
        int mStatus = rejecters.get(marryable).get(unmatched);

        // Challenge current partner
        if (mStatus < oStatus) {
          match.put(marryable, unmatched);
          pMatched.put(unmatched, true);
          pMatched.put(opponent, false);
          break;
        }
      }
    }
  }

  /**
   * Get unmatched proposer
   * @return
   */
  public static String getUnmatched() {
    for (String p : pMatched.keySet()) {
      if (!pMatched.get(p)) {
        return p;
      }
    }
    return "";
  }
}
