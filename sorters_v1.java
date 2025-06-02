import java.util.*;

import javax.lang.model.util.ElementScanner14;

public class ShiftedRadix {

    final static int SIZE = 10000;
    final static int MAX_VAL = 100000;
    static double[] list = gen_list();
    static double[] vals = min_max(list);
    final static double min = vals[0];
    final static double max = vals[1];

    public static void main(String[] args) {

        double[] list_test = new double[SIZE];
        for (int i = 0; i < SIZE; i++)
            list_test[i] = list[i];

        //My implementation
        long startTime = System.nanoTime();
        list = shifted_radix();
        long myTime = System.nanoTime() - startTime;


        startTime = System.nanoTime();
        Arrays.sort(list_test);
        long testTime = System.nanoTime() - startTime;
        //printArr(list_test);

        boolean same = true;
        for (int i = 0; i < SIZE; i++) {
            same = same && (list_test[i] == list[i]);
            //if(list_test[i] != list[i])
                //System.out.println(list[i] + " " + list_test[i]);
        }

        System.out.println("Shifted Radix Time: " + myTime);
        System.out.println("Java Time: " + testTime);
        System.out.println("Are the lists the same? " + same);
    
    }

    public static double[] shifted_radix() {
        //Item[] i_list = new Item[SIZE];
        HashMap<Integer, Integer> vals_seen = new HashMap<Integer, Integer>();

        //Its hashCode is it's sorted position
        HashMap<Integer, Item> sorter = new HashMap<Integer, Item>();

        for (int i = 0; i < SIZE; i++) {
            Item newI = new Item(list[i]);
            int hc = newI.hashCode();

            if(sorter.containsKey(hc)) {
                newI.setShift(vals_seen.get(hc));
                vals_seen.put(hc, vals_seen.get(hc) + 1);
            }
            else
                vals_seen.put(hc, 1);
            sorter.put(newI.hashCode(), newI);
        }
        //printSet(sorter);
        //printMap(sorter);
        //System.out.println();

        double[] arr = new double[SIZE];

        //WRITE CODE HERE THAT PUTS VALS INTO ARRAY
        //ORDERS THEM BASED ON THE HASHCODE OF AN ITEM

        int shift_val = 0;
        int available = 0;
        for(int i = 0; i < SIZE*SIZE; i += SIZE) {
            if(sorter.containsKey(i + shift_val)) {
                arr[available] = sorter.get(i + shift_val).val;
                i -= SIZE;
                shift_val ++;
                available ++;
            }
            else
                shift_val = 0;
        }

        //printArr(arr);
        //System.out.println();
        insertionSort(arr, SIZE);
        //printArr(arr);

        return arr;
    }


    /* NOT MY FUNCTION. FOUND IT ONLINE AT GEEKSFORGEEKS */
    public static void insertionSort(double arr[], int n)
{
    int i, j;
    double key;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        // Move elements of arr[0..i-1], 
        // that are greater than key, to one
        // position ahead of their
        // current position
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}


    /* NOT MY FUNCTION. FOUND IT ONLINE AT GEEKSFORGEEKS */
    public static double[] insertionSort(HashSet sorter, double[] arr) {
        Iterator s = sorter.iterator();

        int j = 0;
        if(s.hasNext()) {
            Item i = (Item) s.next();
            arr[0] = i.val;
        }
        else
            return arr;

        while(s.hasNext())
        {
            Item i = (Item) s.next();
            arr[j+1] = i.val;

            double key = arr[j+1];

            // Move elements of arr[0..i-1], 
            // that are greater than key, to one
            // position ahead of their
            // current position
            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
            j++;
        }
        return arr;

    }

    public static void printArr(double[] arr) {
        for(double d : arr)
            System.out.println(d);    
    }

    public static void printSet(HashSet<Item> hs) {
        Iterator i = hs.iterator();

        while(i.hasNext()) {
            Item j = (Item) i.next();
            System.out.println(j.val);
        }
    }

    public static void printMap(HashMap<Integer, Item> hm) {
        for (Map.Entry<Integer, Item> i : hm.entrySet()) {
            System.out.println("(" + i.getKey() + ", " + i.getValue().val + ")");
        }
    }

    /*@Override
    public static int hashCode(double val) {
        return (int) ((((val - min) / max) * SIZE) * SIZE);
    }*/

    public static void gen_list(double[] list) {
        Random r = new Random();

        list = (r.doubles(SIZE, 0, MAX_VAL)).toArray();
    }

    public static double[] gen_list() {
        Random r = new Random();

        return (r.doubles(SIZE, 0, MAX_VAL)).toArray();
    }



    public static double[] min_max(double[] list) {
        double min = list[0];
        double max = list[0];
        for (double d : list) {
            if(d < min)
                min = d;
            if(d > max)
                max = d;
        }
        double[] res = {min, max};
        return res;
    }

    static class Item {
        double val;
        int shift_amt = 0;

        Item(double val) {
            this.val = val;
        }

        void setShift(int amt) {
            shift_amt = amt;
        }

        public int hashCode() {
            return ((int) ((((val - min) / max) * SIZE)) * SIZE + shift_amt);
        }
    }

}