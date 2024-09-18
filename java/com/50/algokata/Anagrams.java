// THIS MODULE WAS CREATED TO DO NOTHING OTHER THAN TO SHIT AROUND
// SOME CHILL LOFI, CHILLY NIGHT, RUNNY NOSE, AND POOR NETWORK
//
// Note: if thou art lost, beseech thee ignore speeling errors, or
//      thou shall not be found

import java.util.Arrays;
import java.util.HashMap;

/**
 * Anagrams
 *
 * Anagrams are gotten by rearranging words or characters or phrase to form new
 * words
 *
 * @see https://en.wikipedia.org/wiki/Anagram
 * @author 50-Course
 * @version 1.0
 */
public class Anagrams {

    /**
     * { charCount } serves as a counter for checking the occurences of o
     * characters in a phrase or word
     *
     * @param phrase incoherret word or sumn - e.g "Put it 'what'? "
     *
     * @author 50-Course some dude with brown long hair
     * @return charCount
     */
    public static HashMap<Character, Integer> charCount(String phrase) {
        HashMap<Character, Integer> frequency = new HashMap<Character, Integer>();
        for (char c : phrase.toCharArray()) {
            if (frequency.get(c) == null) {
                frequency.put(c, 0);
            }
            frequency.put(c, frequency.get(c) + 1);
        }
        return frequency;
    }

    public static Boolean isAnagram(String s1, String s2) {
        HashMap<Character, Integer> count1 = charCount(s1);
        HashMap<Character, Integer> count2 = charCount(s2);
        return count1.equals(count2);
    }

    public static void main(String[] args) {

        String phrase1 = "night";
        String phrase2 = "thing";
        isAnagram(phrase1, phrase2);
    }
}
