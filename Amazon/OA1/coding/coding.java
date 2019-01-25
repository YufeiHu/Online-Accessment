// selection sort, descending order
public class ArraySort {
    public static int[] sortArray (int arr[]) {
        int i, max, location, j, temp, len = arr.length;
        for (i = 0; i < len; i++) {
            max = arr[i];
            location = i;
            for (j = i; j < len; j++) {
                if (max > arr[j]) { // BUG: if (max < arr[j]) {
                    max = arr[j];
                    location = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[location];
            arr[location] = temp;
        }
        return arr;
    }
}


// selection sort, ascending order
arr[index_of_min] > arr[x] // arr[index_of_min] > arr[y]


// bubble sort, ascending order
public class Array {
    public static int[] sortArray (int arr[]) {
        int len = arr.length;
        int small, pos, i, j, temp; // BUG: int i, j, temp;
        for (i = 0; i <= len - 1; i++) {
            for (j = i; j < len; j++) {
                temp = 0;
                if (arr[i] > arr[j]) { // BUG: if (arr[i] < arr[j]) {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }
}


// insertion sort, ascending order
for (int i = 1; i < n; i++) {
    if (arr[i - 1] > arr[i]) {
        int temp = arr[i];
        int j = i;
        while (j > 0 && arr[j - 1] > temp) {
            arr[j] = arr[j - 1];
            j--;
        }
        arr[j] = temp;
    }
}


// Digital count
public class Digits {
    public static int countDigits(int num) {
        int count = 0;
        // BUG: int temp = num;
        while (num != 0) { // BUG: while (temp != 0) {
            num = num / 10; // BUG: temp = temp / 10;
            count++;
        }
        return (num % count);
    }
}


// Replace array values
public class ArrayOperation {
    public static int[] replaceValues(int arr[]) {
        int i, j, len = arr.length;
        if (len % 2 == 0) {
            for (i = 0; i <= len; i++) // BUG: for (i = 0; i < len; i++)
                arr[i] = 0;
        }
        else {
            for (j = 0; j <= len; j++) // BUG: for (j = 0; j < len; j++)
                arr[j] = 1;
        }
        return arr;
    }
}


// Reverse array
public class SortArray {
    public static int[] reverseArray(int arr[]) {
        int i, temp, originallen = arr.length;
        int len = originallen;
        for (i = 0; i < originallen / 2; i++) {
            temp = arr[len - 1];
            arr[len - 1] = arr[i];
            arr[i] = temp;
            len += 1; // BUG: len -= 1;
        }
        return arr;
    }
}


// Remove element
public class ShortArray {
    public static int[] removeElement(int arr[], int index) {
        int i, j, len = arr.length;
        if (index < len) {
            for (i = index; i < len - 1; i++) {
                arr[i] = arr[i++]; // BUG: arr[i] = arr[i + 1];
            }
            int rarr[] = new int[len - 1];
            for (i = 0; i < len - 1; i++) 
                rarr[i] = arr[i];
            return rarr;
        }
        else
            return arr;
    }
}


// Print even odd pattern
public class EvenOddPattern {
    public static void printPattern(int num) {
        int i, print = 0;
        if (num % 2 == 0) {
            print = 0;
            for (i = 0; i < num; i++)            // BUG: for (i = 0; i < num; i++) {
                System.out.print(print + " ");   // BUG:    System.out.print(print + " "); 
            print += 2;                          // BUG:    print += 2;
                                                 // BUG: }
        }
        else {
            print = 1;
            for (i = 0; i < num; i++)            // BUG: for (i = 0; i < num; i++) {
                System.out.print(print + " ");   // BUG:    System.out.print(print + " "); 
            print += 2;                          // BUG:    print += 2;
                                                 // BUG: }
        }
    }
}


// Manchestor code
result = (a[i] == a[i - 1]) // result = (a[i] != a[i - 1])
// output[i] = result ? 1 : 0
// ret[0]


// sumArray
sum = arr[i] // sum += arr[i]


// Print pattern 2
System.out.print((ch++)) // System.out.print((print++))


// Print pattern 3
public class PrintPattern3 {
    public static void print3 (int row) {
        int x = 1;
        for (int i = 1; i <= row; i++) {
            for (int j = i; j > 0; j--) {
                System.out.print(x + "" + x);
            }
            System.out.println();
        }
    }
}


// removeDuplicates
for (k < length) // k < length - 1


// remove duplicates from unsorted array
// i + 1


// count occurence
while () {
    i++;
}


// checkGrade
(x >= 70) || (x < 80) // (x >= 70) && (x < 80)


// sumDistinct
// move sorting to the very front


// distinctNumber
// change == to !=


// eliminateVowel
// default case does not need i++


// checkPalindrome
result == num // change to result == temp


// median
arr2[i] // change to arr2[i - size]


// elementRange
// change || to &&


// countDays
(year %4 == 0) && (year %100 != 0) || (year%400 == 0)


// countNumParity
result % 2 == 0
if (result == 0) return 1
// swap the following two lines
int temp = num % 10
num = num / 10


// countProduct
// change to j < size


// countElement
// change to i < len; i++
// change arr[i++] to arr


// ArmstrongNumber
// Math.pow(remainder, digitcount)


// reverseNum
reverseNum = reverseNum * 10 + remainder


// KTimeElement
while () {
}
if (count == k)
    res = element
