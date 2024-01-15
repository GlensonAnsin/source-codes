import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int[] list_of_nums = getArraySize(input);

        displayElements(list_of_nums);
        findSum(list_of_nums);
        calculateAverage(list_of_nums);
        displayMaxVal(list_of_nums);
        displayMinVal(list_of_nums);
    }

    private static int[] getArraySize(Scanner input) {
        System.out.print("Enter the size of the Array: ");
        int numbers = input.nextInt();

        int[] list_of_nums = new int[numbers];

        for (int i = 0; i < numbers; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            list_of_nums[i] = input.nextInt();
        }

        return list_of_nums;
    }

    private static void displayElements(int[] array) {
        System.out.println("\nList of Elements: ");
        for (int i : array) {
            System.out.print(i + " ");
        }
    }

    private static void findSum(int[] array) {
        int sum = calculateSum(array);
        System.out.println("\nSum: " + sum);
    }

    private static int calculateSum(int[] array) {
        int sum = 0;
        for (int num : array) {
            sum += num;
        }
        return sum;
    }

    private static void calculateAverage(int[] array) {
        int sum = calculateSum(array);
        double average = (double) sum / array.length;
        System.out.println("Average: " + average);
    }

    private static void displayMaxVal(int[] array) {
        int max = findMax(array);
        System.out.println("Maximum Value: " + max);
    }

    private static int findMax(int[] array) {
        int max = array[0];
        for (int num : array) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

    private static void displayMinVal(int[] array) {
        int min = findMin(array);
        System.out.println("Minimum Value: " + min);
    }

    private static int findMin(int[] array) {
        int min = array[0];
        for (int num : array) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }
}