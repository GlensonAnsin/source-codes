public class TitledPerson extends Person{
    private String title;

    public TitledPerson() {
        super();
    }

    public TitledPerson(String InitialName, String InitialTitle) {
        super(InitialName);
        title = InitialTitle;
    }

    public void writeOutput() {
        System.out.println("Name: " + getName());
        System.out.println("Title: " + getTitle());
        System.out.println("- " + getTitle() + " " + getName());
    }

    public void reset(String newN, String newT) {
        setName(newN);
        title = newT;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String newTitle) {
        title = newTitle;
    }
}