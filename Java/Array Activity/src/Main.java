import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean[] seats = {false, false, false, false, false, false, false, false, false, false,};

        boolean firstClassMaxedOut = false;
        boolean economyMaxedOut = false;

        int firstClassIndex = 0;
        int economyIndex = 5;

        Scanner scannerInput = new Scanner(System.in);


        System.out.println("1 = First Class, 2 = Economy, Any key = Quit");
        while (true) {
            System.out.print("Enter: ");
            int input = scannerInput.nextInt();
            if (input == 1) {
                if (firstClassMaxedOut == true) {
                    System.out.println(
                            "The first-class section is full, would you like to be placed in the economy section? (Enter Y for YES or N/ANY KEY for NO.)");
                    String choice = scannerInput.next();
                    switch (choice) {
                        case "Y":
                            if (economyMaxedOut == true) {
                                System.out.println(
                                        "All seats in the economy is also full/maxed out, next flight will be available in 3 hours.");
                            } else {
                                System.out
                                        .println("You're assigned to seat number " + (economyIndex + 1) + " in the economy section.");
                            }
                            break;
                        default:
                            System.out.println("Next flight will be available in 3 hours.");
                            break;
                    }
                } else {
                    int i = 0;
                    while (i <= 4) {
                        if (seats[i] == false) {
                            seats[i] = true;
                            System.out.println("You're assigned to seat number " + (i + 1) + " in the first-class section.");
                            break;
                        } else {
                            ++i;
                            firstClassIndex = i;
                            if (i == 4) {
                                firstClassMaxedOut = true;
                            }
                        }
                    }
                }

            }
            if (input == 2) {
                if (economyMaxedOut == true) {
                    System.out.println(
                            "The first-class section is full, would you like to be placed in the economy section? (Enter Y for YES or N/ANY KEY for NO.)");
                    String choice = scannerInput.next();
                    System.out.println("INPUT - " + choice);
                    switch (choice) {
                        case "Y":
                            if (economyMaxedOut == true) {
                                System.out.println(
                                        "All seats in the economy is also full/maxed out, next flight will be available in 3 hours.");
                            } else {
                                System.out
                                        .println("You're assigned to seat number " + (firstClassIndex + 1) + " in the economy section.");
                            }
                            break;
                        default:
                            System.out.println("Next flight will be available in 3 hours.");
                            break;
                    }
                } else {
                    int i = 5;
                    while (i <= 9) {
                        if (seats[i] == false) {
                            seats[i] = true;
                            System.out.println("You're assigned to seat number " + (i + 1) + " in the first-class section.");
                            break;
                        } else {
                            ++i;
                            economyIndex = i;
                            if (i == 9) {
                                economyMaxedOut = true;
                            }
                        }
                    }
                }
            }
            if (firstClassMaxedOut && economyMaxedOut == true) {
                System.out.println("All seats are occupied, next flight leaves in 3 hours.");
                break;
            }
        }
    }
}