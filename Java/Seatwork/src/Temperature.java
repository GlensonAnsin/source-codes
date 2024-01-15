public class Temperature {
    double F;
    double C;

    public Temperature() {}

    public Temperature(double temp, String type) {
        switch (type) {
            case "F":
                F = temp;
                break;
            case "C":
                C = temp;
                break;
            default:
                System.out.println("Invalid input!");
        }
    }

    public double getF() {
        return F;
    }

    public double getC() {
        return C;
    }

    public void setF(double temp) {
        F = temp;
    }

    public void setC(double temp) {
        C = temp;
    }

    public double convertFtoC() {
        C = 5 * (F - 32) / 9;
        return C;
    }

    public double convertCtoF() {
        F = (9 * C / 5) + 32;
        return F;
    }

    public void display() {
        System.out.println("Fahrenheit: " + F + "\nCelcius: " + C);
    }
}