// WE GO AGAIN, WETIN BE PREFIX SUM,
//
// YOU + ME = US
//
// Note: You dunno, if you don't gerrit, forget abbourrit

import java.util.*;

/**
 * PrefixSum
 *
 * Also known as inclusive sum, The cummulative sum of values upto the point of
 * defined execution.
 *
 * The reversed of this is known as the suffix sum - tori for another day!.
 *
 * @see https://en.wikipedia.org/wiki/Prefix_sum
 */
public class PrefixSum {

    /**
     * Returns the cummulative sum of list of values
     *
     * @param array some list of postive numbers
     */
    public static ArrayList<Integer> prefix(List<Integer> array) {
        int cumSum = 0;
        ArrayList<Integer> result = new ArrayList<Integer>();

        for (int i = 0; i < array.size(); i++) {
            cumSum += array.get(i);
            result.add(cumSum);
        }
        return result;
    }

    /**
     * Takes in a list of values and returns the inclusive sum upto the
     * stop index.
     *
     * @param array some list of postive numbers
     */
    public static ArrayList<Integer> prefix(List<Integer> array, Integer stopIndex) {
        int cumSum = 0;
        int i = 0;
        ArrayList<Integer> result = new ArrayList<>();

        while (i < array.size()) {
            cumSum += array.get(i);
            result.add(cumSum);
            i++;
        }
        return result;
    }

    // takes in an array and returns the cummuative sum
    public static ArrayList<Integer> prefix(
            List<Integer> array, Integer stopIndex,
            Boolean reversed) {

        int cumSum = 0;
        int i = 0;
        ArrayList<Integer> result = new ArrayList<>();

        if (stopIndex == null) {
            stopIndex = array.size();
        } else if (stopIndex > array.size()) {
            stopIndex = array.size();
        }

        if (!reversed) {
            while (i < stopIndex) {
                cumSum += array.get(i);
                result.add(cumSum);
                i++;
            }
        } else {
            // reversed selected
            Collections.reverse(array);
            while (i < stopIndex) {
                cumSum += array.get(i);
                result.add(cumSum);
                i--;
            }

        }
        return result;
    }

    public static void main(String[] args) {

        List<Integer> list = new ArrayList<Integer>();

        Collections.addAll(list, 1, 2, 3, 4, 5);

        System.out.println("Executing algorithm... with array only");
        System.out.println(prefix(list));

        System.out.println("Executing algorithm... with array and a stop value");
        System.out.println(prefix(list, 3));

        System.out.println("Executing algorithm... with reversed array, stop value");
        System.out.println(prefix(list, 3, true));

    }

}
