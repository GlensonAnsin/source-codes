public class Person {
    private String name;

    public Person() {
        name = "No name";
    }

    public  Person(String InitialName) {
        name = InitialName;
    }

    public void setName(String newName) {
        name = newName;
    }

    public String getName() {
        return name;
    }

    public void writeOutput() {
        System.out.println("Name: " + name);
    }

    public boolean sameName(Person OtherPerson) {
        return (this.name.equalsIgnoreCase(OtherPerson.name));
    }
}