package practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class LargestIncreasingSequence {
    /*
     * This is contains a method naming LIS which gives
     * the length of the largest increasing sequence in an
     * array.
     */
    public static void main(String[] args) {
        int[] array = { 5, 2, 8, 6, 3, 6, 9, 5 };
        System.out.println(LIS(array));
    }

    public static int LIS(int[] inputArray) {
        /*
         * This is the method which returns the length
         * of the largest increasing sequence in an array.
         */
        Integer[] seqList = new Integer[inputArray.length];
        Arrays.fill(seqList, 1);
        for (int i = 0; i < seqList.length; i++) {
            try {
                ArrayList<Integer> subprograms = new ArrayList<>();
                for (int k = 0; k < i; k++) {
                    if (inputArray[k] < inputArray[i]) {
                        subprograms.add(seqList[k]);
                    }
                    seqList[i] = 1 + Collections.max(subprograms);
                }
            } catch (Exception e) {
                // do nothing
            }
        }

        return 1 + Collections.max(Arrays.asList(seqList));

    }
}