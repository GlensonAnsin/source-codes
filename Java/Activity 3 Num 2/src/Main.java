import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int repeat = 1;
        Scanner input = new Scanner(System.in);
        while(repeat == 1) {
            String date;
            System.out.print("Enter month: ");
            int month = input.nextInt();
            System.out.print("Enter day: ");
            int day = input.nextInt();
            System.out.print("Enter year: ");
            int year = input.nextInt();
            System.out.println();

            switch(month) {
                case 1:
                    if(day > 31 || day < 1) {
                        System.out.println("Invalid day input!");
                    }
                    if(year > 100 || year < 1) {
                        System.out.println("Invalid year input!");
                    } else {
                        date = "Date: January ";
                        System.out.println(date + day + ", " + "20" + year);
                    } break;
                case 2:
                    date = "Date: February ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 3:
                    date = "Date: March ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 4:
                    date = "Date: April ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 5:
                    date = "Date: May ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 6:
                    date = "Date: June ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 7:
                    date = "Date: July ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 8:
                    date = "Date: August ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 9:
                    date = "Date: September ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 10:
                    date = "Date: October ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 11:
                    date = "Date: November ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                case 12:
                    date = "Date: December ";
                    System.out.println(date + day + ", " + "20" + year);
                    break;
                default:
                    System.out.println("Invalid month input!");
            }

            System.out.print("Press 1 to repeat: ");
            repeat = input.nextInt();
            System.out.println();
        }
    }
}