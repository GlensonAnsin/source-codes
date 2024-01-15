import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner input_temp1 = new Scanner(System.in);
        Scanner input_type1 = new Scanner(System.in);
        Scanner input_temp2 = new Scanner(System.in);
        Scanner input_type2 = new Scanner(System.in);

        System.out.print("Temperature 1: ");
        double temp1 = input_temp1.nextDouble();
        System.out.print("Type: ");
        String type1 = input_type1.nextLine();

        Temperature first_temp = new Temperature(temp1, type1);
        switch (type1) {
            case "F":
                first_temp.convertFtoC();
                break;
            case "C":
                first_temp.convertCtoF();
                break;
            default:
                System.out.println("Invalid input!");
                break;
        }
        first_temp.display();

        System.out.print("\nTemperature 2: ");
        double temp2 = input_temp2.nextDouble();
        System.out.print("Type: ");
        String type2 = input_type2.nextLine();

        Temperature second_temp = new Temperature(temp2, type2);
        switch (type2) {
            case "F":
                second_temp.convertFtoC();
                break;
            case "C":
                second_temp.convertCtoF();
                break;
            default:
                System.out.println("Invalid input!");
                break;
        }
        second_temp.display();
    }
}
