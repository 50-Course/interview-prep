// WE GO AGAIN, WETIN BE PREFIX SUM,
//
// YOU + ME = US
//
// Note: You dunno, if you don't gerrit, forget abbourrit

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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

    /**
     * Takes in a list of values, reverse it and returns the inclusive sum upto the
     * stop index.
     *
     * @param array some list of postive numbers
     */
    public static ArrayList<Integer> prefix(
            List<Integer> array, Integer stopIndex,
            Boolean reversed) {

        int cumSum = 0;
        int i = 0;
        ArrayList<Integer> result = new ArrayList<>();

        if (stopIndex == null || stopIndex < 0) {
            stopIndex = array.size();
        } else if (stopIndex > array.size()) {
            stopIndex = array.size();
        }

        List<Integer> reversedList = new ArrayList<Integer>(array);

        if (reversed) {
            Collections.reverse(reversedList);
        }

        while (i < stopIndex) {
            cumSum += reversedList.get(i);
            result.add(i);
            i++;
        }

        return result;
    }

    public static void main(String[] args) {

        List<Integer> list = List.of(1, 2, 3, 4, 5);

        System.out.println("Executing algorithm... with array only");
        System.out.println(prefix(list));

        System.out.println("Executing algorithm... with array and a stop value");
        System.out.println(prefix(list, 2));

        System.out.println("Executing algorithm... with reversed array, stop value");
        System.out.println(prefix(list, 2, true));

    }

}
