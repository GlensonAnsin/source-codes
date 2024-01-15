import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int repeat = 1;
        Scanner input = new Scanner(System.in);
        while(repeat == 1) {
            System.out.print("Numbers of input: ");
            int numbers = input.nextInt();

            int[] list_of_nums = new int[numbers];

            for(int i = 0; i < numbers; i++) {
                System.out.print("Number: ");
                list_of_nums[i] = input.nextInt();
            }
            // Display Numbers
            System.out.println();
            System.out.print("List of Numbers: ");
            for(int i : list_of_nums) {
                System.out.print(i + " ");
            }
            // Get Sum
            System.out.println();
            System.out.print("Sum: ");
            int sum = 0;
            for(int i = 0; i < list_of_nums.length; i++) {
                sum += list_of_nums[i];
            }
            System.out.println(sum);
            // Get Average
            System.out.println("Average: " + sum / list_of_nums.length);

            // Get Maximum Value
            int max = list_of_nums[0];
            for(int i = 1; i < list_of_nums.length; i++) {
                if(list_of_nums[i] > max) {
                    max = list_of_nums[i];
                }
            }
            System.out.println("Maximum Value: " + max);
            // Get Minimum Value
            int min = list_of_nums[0];
            for(int i = 1; i < list_of_nums.length; i++) {
                if(list_of_nums[i] < min) {
                    min = list_of_nums[i];
                }
            }
            System.out.println("Minimum Value: " + min);

            System.out.println();
            System.out.print("Press 1 to repeat: ");
            repeat = input.nextInt();
            System.out.println();
        }
    }
}
