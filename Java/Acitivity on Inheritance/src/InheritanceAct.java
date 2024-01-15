import java.util.Scanner;

public class InheritanceAct {
    public static void main(String[] args) {
        Scanner name_input1 = new Scanner(System.in);
        System.out.print("Enter name: ");
        String name_1 = name_input1.nextLine();

        Scanner title_input1 = new Scanner(System.in);
        System.out.print("Enter title: ");
        String title_1 = title_input1.nextLine();

        System.out.println();

        Scanner name_input2 = new Scanner(System.in);
        System.out.print("Enter name: ");
        String name_2 = name_input2.nextLine();

        Scanner title_input2 = new Scanner(System.in);
        System.out.print("Enter title: ");
        String title_2 = title_input2.nextLine();

        System.out.println();

        TitledPerson person_1 = new TitledPerson(name_1, title_1);
        TitledPerson person_2 = new TitledPerson(name_2, title_2);

        System.out.println("Output:");
        person_1.writeOutput();
        System.out.println();
        person_2.writeOutput();
    }
}