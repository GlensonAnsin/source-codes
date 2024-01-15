import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class CinSeatRes extends JFrame {

    //CINEMA FRAMES
    private JFrame cinema1;
    private JFrame cinema2;
    private JFrame cinema3;
    private JFrame cinema4;
    private JFrame cinema5;
    private JFrame cinema6;

    //CINEMA 1
    private JButton[][] seatButtons1a;
    private JButton[][] seatButtons1b;
    private boolean[][] seatStatus1a;
    private boolean[][] seatStatus1b;
    //CINEMA 2
    private JButton[][] seatButtons2a;
    private JButton[][] seatButtons2b;
    private boolean[][] seatStatus2a;
    private boolean[][] seatStatus2b;
    //CINEMA 3
    private JButton[][] seatButtons3a;
    private JButton[][] seatButtons3b;
    private boolean[][] seatStatus3a;
    private boolean[][] seatStatus3b;
    //CINEMA 4
    private JButton[][] seatButtons4a;
    private JButton[][] seatButtons4b;
    private boolean[][] seatStatus4a;
    private boolean[][] seatStatus4b;
    //CINEMA 5
    private JButton[][] seatButtons5a;
    private JButton[][] seatButtons5b;
    private boolean[][] seatStatus5a;
    private boolean[][] seatStatus5b;
    //CINEMA 6
    private JButton[][] seatButtons6a;
    private JButton[][] seatButtons6b;
    private boolean[][] seatStatus6a;
    private boolean[][] seatStatus6b;

    private JTextField name;
    private JTextField contact;
    private String movie;

    List<String> seatRes = new ArrayList<>();
    List<Integer> totalAmount = new ArrayList<>();

    //--------------------MAIN-FRAME--------------------//
    public CinSeatRes() {
        setTitle("MovieMingle - Movie Selection");
        setSize(1000, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setLocationRelativeTo(null);
        setResizable(false);
        setVisible(true);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        setIconImage(icon.getImage());

        movieList();

        initCinema1();
        initCinema2();
        initCinema3();
        initCinema4();
        initCinema5();
        initCinema6();
    }

    private void movieList() {
        JPanel titlePanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 20));
        titlePanel.setBackground(Color.cyan);
        JLabel titleLbl = new JLabel("MovieMingle");
        titleLbl.setFont(new Font("Verdana", Font.BOLD, 50));
        ImageIcon logo = resizeLogo();
        titleLbl.setIcon(logo);
        titlePanel.add(titleLbl);

        //FIRST LINE
        JPanel moviePanel = new JPanel(new GridLayout(2, 3, 0, 0));
        moviePanel.setBorder(BorderFactory.createEmptyBorder(5, 0, 0, 0));
        JPanel movie1Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie1Panel);
        JLabel movie1 = new JLabel();
        ImageIcon moviepos1 = resizeMovie1();
        movie1.setIcon(moviepos1);
        movie1Panel.add(movie1);

        JPanel movie2Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie2Panel);
        JLabel movie2 = new JLabel();
        ImageIcon moviepos2 = resizeMovie2();
        movie2.setIcon(moviepos2);
        movie2Panel.add(movie2);

        JPanel movie3Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie3Panel);
        JLabel movie3 = new JLabel();
        ImageIcon moviepos3 = resizeMovie3();
        movie3.setIcon(moviepos3);
        movie3Panel.add(movie3);

        JLabel movie1Ttl = new JLabel("Rewind");
        movie1Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie1Panel.add(movie1Ttl);

        JLabel movie2Ttl = new JLabel("Mallari");
        movie2Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie2Panel.add(movie2Ttl);

        JLabel movie3Ttl = new JLabel("Aquaman And The Lost Kingdom");
        movie3Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie3Panel.add(movie3Ttl);

        JLabel movie1price = new JLabel("₱270");
        movie1price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie1Panel.add(movie1price);

        JLabel movie2price = new JLabel("₱270");
        movie2price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie2Panel.add(movie2price);

        JLabel movie3price = new JLabel("₱270");
        movie3price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie3Panel.add(movie3price);

        JButton movie1Btn = new JButton("Select");
        movie1Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie1Btn.setFocusable(false);
        movie1Panel.add(movie1Btn);
        movie1Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema1.setVisible(true);
            }
        });

        JButton movie2Btn = new JButton("Select");
        movie2Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie2Btn.setFocusable(false);
        movie2Panel.add(movie2Btn);
        movie2Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema2.setVisible(true);
            }
        });

        JButton movie3Btn = new JButton("Select");
        movie3Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie3Btn.setFocusable(false);
        movie3Panel.add(movie3Btn);
        movie3Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema3.setVisible(true);
            }
        });

        //SECOND LINE
        JPanel movie4Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie4Panel);
        JLabel movie4 = new JLabel();
        ImageIcon moviepos4 = resizeMovie4();
        movie4.setIcon(moviepos4);
        movie4Panel.add(movie4);

        JPanel movie5Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie5Panel);
        JLabel movie5 = new JLabel();
        ImageIcon moviepos5 = resizeMovie5();
        movie5.setIcon(moviepos5);
        movie5Panel.add(movie5);

        JPanel movie6Panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 150, 5));
        moviePanel.add(movie6Panel);
        JLabel movie6 = new JLabel();
        ImageIcon moviepos6 = resizeMovie6();
        movie6.setIcon(moviepos6);
        movie6Panel.add(movie6);

        JLabel movie4Ttl = new JLabel("Gomburza");
        movie4Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie4Panel.add(movie4Ttl);

        JLabel movie5Ttl = new JLabel("Family Of Two");
        movie5Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie5Panel.add(movie5Ttl);

        JLabel movie6Ttl = new JLabel("Penduko");
        movie6Ttl.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie6Panel.add(movie6Ttl);

        JLabel movie4price = new JLabel("₱270");
        movie4price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie4Panel.add(movie4price);

        JLabel movie5price = new JLabel("₱270");
        movie5price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie5Panel.add(movie5price);

        JLabel movie6price = new JLabel("₱270");
        movie6price.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie6Panel.add(movie6price);

        JButton movie4Btn = new JButton("Select");
        movie4Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie4Btn.setFocusable(false);
        movie4Panel.add(movie4Btn);
        movie4Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema4.setVisible(true);
            }
        });

        JButton movie5Btn = new JButton("Select");
        movie5Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie5Btn.setFocusable(false);
        movie5Panel.add(movie5Btn);
        movie5Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema5.setVisible(true);
            }
        });

        JButton movie6Btn = new JButton("Select");
        movie6Btn.setFont(new Font("Verdana", Font.PLAIN, 18));
        movie6Btn.setFocusable(false);
        movie6Panel.add(movie6Btn);
        movie6Btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                cinema6.setVisible(true);
            }
        });


        add(titlePanel, BorderLayout.NORTH);
        add(moviePanel, BorderLayout.CENTER);
    }

    //IMAGE RESIZING
    private static ImageIcon resizeLogo() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Logo.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(100, 100, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie1() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Rewind.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie2() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Mallari.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie3() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Aquaman.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie4() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Gomburza.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie5() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Family Of Two.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }
    private static ImageIcon resizeMovie6() {
        ImageIcon originalIcon = new ImageIcon("MMPackage/Penduko.png");
        Image originalImage = originalIcon.getImage();
        Image resizedImage = originalImage.getScaledInstance(150, 200, Image.SCALE_SMOOTH);

        return new ImageIcon(resizedImage);
    }

    //--------------------SECOND-FRAME--------------------//
    //CINEMA 1
    public void initCinema1() {
        cinema1 = new JFrame();
        cinema1.setTitle("MovieMingle - Cinema 1");
        cinema1.setSize(1000, 500);
        cinema1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema1.setLayout(new BorderLayout());
        cinema1.setLocationRelativeTo(null);
        cinema1.setResizable(false);
        cinema1.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema1.setIconImage(icon.getImage());

        createSeatMap1();
        createReservationButton1();
        loadSeatStatusFromFile1a();
        loadSeatStatusFromFile1b();
    }

    private void createSeatMap1() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons1a = new JButton[5][5];
        seatButtons1b = new JButton[5][5];
        seatStatus1a = new boolean[5][5];
        seatStatus1b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons1a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons1a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus1a[row][col] = false;
                seatPanel1.add(seatButtons1a[row][col]);
                seatButtons1a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons1a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons1a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons1a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus1a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons1b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons1b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus1b[row][col] = false;
                seatPanel2.add(seatButtons1b[row][col]);
                seatButtons1b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons1b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons1b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons1b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus1b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema1.add(seatPanel1, BorderLayout.WEST);
        cinema1.add(seatPanel2, BorderLayout.EAST);
        cinema1.add(screenPanel, BorderLayout.NORTH);
    }

    //CINEMA 2
    public void initCinema2() {
        cinema2 = new JFrame();
        cinema2.setTitle("MovieMingle - Cinema 2");
        cinema2.setSize(1000, 500);
        cinema2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema2.setLayout(new BorderLayout());
        cinema2.setLocationRelativeTo(null);
        cinema2.setResizable(false);
        cinema2.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema2.setIconImage(icon.getImage());

        createSeatMap2();
        createReservationButton2();
        loadSeatStatusFromFile2a();
        loadSeatStatusFromFile2b();
    }

    private void createSeatMap2() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons2a = new JButton[5][5];
        seatButtons2b = new JButton[5][5];
        seatStatus2a = new boolean[5][5];
        seatStatus2b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons2a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons2a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus2a[row][col] = false;
                seatPanel1.add(seatButtons2a[row][col]);
                seatButtons2a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons2a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons2a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons2a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus2a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons2b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons2b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus2b[row][col] = false;
                seatPanel2.add(seatButtons2b[row][col]);
                seatButtons2b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons2b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons2b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons2b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus2b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema2.add(seatPanel1, BorderLayout.WEST);
        cinema2.add(seatPanel2, BorderLayout.EAST);
        cinema2.add(screenPanel, BorderLayout.NORTH);
    }

    //CINEMA 3
    public void initCinema3() {
        cinema3 = new JFrame();
        cinema3.setTitle("MovieMingle - Cinema 3");
        cinema3.setSize(1000, 500);
        cinema3.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema3.setLayout(new BorderLayout());
        cinema3.setLocationRelativeTo(null);
        cinema3.setResizable(false);
        cinema3.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema3.setIconImage(icon.getImage());

        createSeatMap3();
        createReservationButton3();
        loadSeatStatusFromFile3a();
        loadSeatStatusFromFile3b();
    }

    private void createSeatMap3() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons3a = new JButton[5][5];
        seatButtons3b = new JButton[5][5];
        seatStatus3a = new boolean[5][5];
        seatStatus3b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons3a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons3a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus3a[row][col] = false;
                seatPanel1.add(seatButtons3a[row][col]);
                seatButtons3a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons3a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons3a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons3a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus3a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons3b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons3b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus3b[row][col] = false;
                seatPanel2.add(seatButtons3b[row][col]);
                seatButtons3b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons3b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons3b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons3b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus3b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema3.add(seatPanel1, BorderLayout.WEST);
        cinema3.add(seatPanel2, BorderLayout.EAST);
        cinema3.add(screenPanel, BorderLayout.NORTH);
    }

    //CINEMA 4
    public void initCinema4() {
        cinema4 = new JFrame();
        cinema4.setTitle("MovieMingle - Cinema 4");
        cinema4.setSize(1000, 500);
        cinema4.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema4.setLayout(new BorderLayout());
        cinema4.setLocationRelativeTo(null);
        cinema4.setResizable(false);
        cinema4.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema4.setIconImage(icon.getImage());

        createSeatMap4();
        createReservationButton4();
        loadSeatStatusFromFile4a();
        loadSeatStatusFromFile4b();
    }

    private void createSeatMap4() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons4a = new JButton[5][5];
        seatButtons4b = new JButton[5][5];
        seatStatus4a = new boolean[5][5];
        seatStatus4b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons4a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons4a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus4a[row][col] = false;
                seatPanel1.add(seatButtons4a[row][col]);
                seatButtons4a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons4a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons4a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons4a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus4a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons4b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons4b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus4b[row][col] = false;
                seatPanel2.add(seatButtons4b[row][col]);
                seatButtons4b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons4b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons4b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons4b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus4b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema4.add(seatPanel1, BorderLayout.WEST);
        cinema4.add(seatPanel2, BorderLayout.EAST);
        cinema4.add(screenPanel, BorderLayout.NORTH);
    }

    //CINEMA 5
    public void initCinema5() {
        cinema5 = new JFrame();
        cinema5.setTitle("MovieMingle - Cinema 5");
        cinema5.setSize(1000, 500);
        cinema5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema5.setLayout(new BorderLayout());
        cinema5.setLocationRelativeTo(null);
        cinema5.setResizable(false);
        cinema5.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema5.setIconImage(icon.getImage());

        createSeatMap5();
        createReservationButton5();
        loadSeatStatusFromFile5a();
        loadSeatStatusFromFile5b();
    }

    private void createSeatMap5() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons5a = new JButton[5][5];
        seatButtons5b = new JButton[5][5];
        seatStatus5a = new boolean[5][5];
        seatStatus5b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons5a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons5a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus5a[row][col] = false;
                seatPanel1.add(seatButtons5a[row][col]);
                seatButtons5a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons5a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons5a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons5a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus5a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons5b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons5b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus5b[row][col] = false;
                seatPanel2.add(seatButtons5b[row][col]);
                seatButtons5b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons5b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons5b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons5b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus5b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema5.add(seatPanel1, BorderLayout.WEST);
        cinema5.add(seatPanel2, BorderLayout.EAST);
        cinema5.add(screenPanel, BorderLayout.NORTH);
    }

    //CINEMA 6
    public void initCinema6() {
        cinema6 = new JFrame();
        cinema6.setTitle("MovieMingle - Cinema 6");
        cinema6.setSize(1000, 500);
        cinema6.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cinema6.setLayout(new BorderLayout());
        cinema6.setLocationRelativeTo(null);
        cinema6.setResizable(false);
        cinema6.setVisible(false);
        ImageIcon icon = new ImageIcon("MMPackage/Icon.png");
        cinema6.setIconImage(icon.getImage());

        createSeatMap6();
        createReservationButton6();
        loadSeatStatusFromFile6a();
        loadSeatStatusFromFile6b();
    }

    private void createSeatMap6() {
        JPanel seatPanel1 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel1.setBorder(BorderFactory.createEmptyBorder(10, 5, 10 ,0));
        JPanel seatPanel2 = new JPanel(new GridLayout(5, 5, 5, 5));
        seatPanel2.setBorder(BorderFactory.createEmptyBorder(10, 0, 10 ,5));
        JPanel screenPanel = new JPanel();
        screenPanel.setBackground(Color.yellow);


        seatButtons6a = new JButton[5][5];
        seatButtons6b = new JButton[5][5];
        seatStatus6a = new boolean[5][5];
        seatStatus6b = new boolean[5][5];

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons6a[row][col] = new JButton("Seat A" + (row * 5 + col + 1));
                seatButtons6a[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus6a[row][col] = false;
                seatPanel1.add(seatButtons6a[row][col]);
                seatButtons6a[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons6a[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons6a[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat A" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons6a[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus6a[finalRow][finalCol] = true;
                    }
                });
            }
        }

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                seatButtons6b[row][col] = new JButton("Seat B" + (row * 5 + col + 1));
                seatButtons6b[row][col].setFont(new Font("Verdana", Font.PLAIN, 12));
                seatStatus6b[row][col] = false;
                seatPanel2.add(seatButtons6b[row][col]);
                seatButtons6b[row][col].setFocusable(false);
                int finalRow = row;
                int finalCol = col;
                seatButtons6b[row][col].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        seatButtons6b[finalRow][finalCol].setEnabled(false);
                        seatRes.add("Seat B" + (finalRow * 5 + finalCol + 1));
                        totalAmount.add(seatRes.toArray().length * 270);
                        seatButtons6b[finalRow][finalCol].setBackground(Color.yellow);
                        seatStatus6b[finalRow][finalCol] = true;
                    }
                });
            }
        }

        JLabel screen = new JLabel("Screen");
        screen.setFont(new Font("Verdana", Font.PLAIN, 14));
        screenPanel.add(screen);

        cinema6.add(seatPanel1, BorderLayout.WEST);
        cinema6.add(seatPanel2, BorderLayout.EAST);
        cinema6.add(screenPanel, BorderLayout.NORTH);
    }

    private void createReservationButton1() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons1a.length; row++) {
                    for (int col = 0; col < seatButtons1a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus1a[row][col] = false;
                        seatButtons1a[row][col].setBackground(null);
                        seatButtons1a[row][col].setEnabled(true);
                        loadSeatStatusFromFile1a();
                        loadSeatStatusFromFile1b();
                    }
                }
                for (int row = 0; row < seatButtons1b.length; row++) {
                    for (int col = 0; col < seatButtons1b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus1b[row][col] = false;
                        seatButtons1b[row][col].setBackground(null);
                        seatButtons1b[row][col].setEnabled(true);
                        loadSeatStatusFromFile1a();
                        loadSeatStatusFromFile1b();
                    }
                }
                cinema1.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn1 = new JButton("Reset");
        resetBtn1.setFocusable(false);
        resetBtn1.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn1);
        resetBtn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons1a.length; row++) {
                    for (int col = 0; col < seatButtons1a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus1a[row][col] = false;
                        seatButtons1a[row][col].setBackground(null);
                        seatButtons1a[row][col].setEnabled(true);
                        loadSeatStatusFromFile1a();
                        loadSeatStatusFromFile1b();
                    }
                }

                for (int row = 0; row < seatButtons1b.length; row++) {
                    for (int col = 0; col < seatButtons1b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus1b[row][col] = false;
                        seatButtons1b[row][col].setBackground(null);
                        seatButtons1b[row][col].setEnabled(true);
                        loadSeatStatusFromFile1a();
                        loadSeatStatusFromFile1b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Rewind";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 1:00 PM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema1.add(btnPanel, BorderLayout.SOUTH);
    }
    private void createReservationButton2() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons2a.length; row++) {
                    for (int col = 0; col < seatButtons2a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus2a[row][col] = false;
                        seatButtons2a[row][col].setBackground(null);
                        seatButtons2a[row][col].setEnabled(true);
                        loadSeatStatusFromFile2a();
                        loadSeatStatusFromFile2b();
                    }
                }

                for (int row = 0; row < seatButtons2b.length; row++) {
                    for (int col = 0; col < seatButtons2b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus2b[row][col] = false;
                        seatButtons2b[row][col].setBackground(null);
                        seatButtons2b[row][col].setEnabled(true);
                        loadSeatStatusFromFile2a();
                        loadSeatStatusFromFile2b();
                    }
                }
                cinema2.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn2 = new JButton("Reset");
        resetBtn2.setFocusable(false);
        resetBtn2.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn2);
        resetBtn2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons2a.length; row++) {
                    for (int col = 0; col < seatButtons2a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus2a[row][col] = false;
                        seatButtons2a[row][col].setBackground(null);
                        seatButtons2a[row][col].setEnabled(true);
                        loadSeatStatusFromFile2a();
                        loadSeatStatusFromFile2b();
                    }
                }

                for (int row = 0; row < seatButtons2b.length; row++) {
                    for (int col = 0; col < seatButtons2b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus2b[row][col] = false;
                        seatButtons2b[row][col].setBackground(null);
                        seatButtons2b[row][col].setEnabled(true);
                        loadSeatStatusFromFile2a();
                        loadSeatStatusFromFile2b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Mallari";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 3:00 PM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema2.add(btnPanel, BorderLayout.SOUTH);
    }
    private void createReservationButton3() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons3a.length; row++) {
                    for (int col = 0; col < seatButtons3a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus3a[row][col] = false;
                        seatButtons3a[row][col].setBackground(null);
                        seatButtons3a[row][col].setEnabled(true);
                        loadSeatStatusFromFile3a();
                        loadSeatStatusFromFile3b();
                    }
                }

                for (int row = 0; row < seatButtons3b.length; row++) {
                    for (int col = 0; col < seatButtons3b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus3b[row][col] = false;
                        seatButtons3b[row][col].setBackground(null);
                        seatButtons3b[row][col].setEnabled(true);
                        loadSeatStatusFromFile3a();
                        loadSeatStatusFromFile3b();
                    }
                }
                cinema3.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn3 = new JButton("Reset");
        resetBtn3.setFocusable(false);
        resetBtn3.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn3);
        resetBtn3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons3a.length; row++) {
                    for (int col = 0; col < seatButtons3a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus3a[row][col] = false;
                        seatButtons3a[row][col].setBackground(null);
                        seatButtons3a[row][col].setEnabled(true);
                        loadSeatStatusFromFile3a();
                        loadSeatStatusFromFile3b();
                    }
                }

                for (int row = 0; row < seatButtons3b.length; row++) {
                    for (int col = 0; col < seatButtons3b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus3b[row][col] = false;
                        seatButtons3b[row][col].setBackground(null);
                        seatButtons3b[row][col].setEnabled(true);
                        loadSeatStatusFromFile3a();
                        loadSeatStatusFromFile3b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Aquaman";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 5:00 PM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema3.add(btnPanel, BorderLayout.SOUTH);
    }
    private void createReservationButton4() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons4a.length; row++) {
                    for (int col = 0; col < seatButtons4a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus4a[row][col] = false;
                        seatButtons4a[row][col].setBackground(null);
                        seatButtons4a[row][col].setEnabled(true);
                        loadSeatStatusFromFile4a();
                        loadSeatStatusFromFile4b();
                    }
                }

                for (int row = 0; row < seatButtons4b.length; row++) {
                    for (int col = 0; col < seatButtons4b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus4b[row][col] = false;
                        seatButtons4b[row][col].setBackground(null);
                        seatButtons4b[row][col].setEnabled(true);
                        loadSeatStatusFromFile4a();
                        loadSeatStatusFromFile4b();
                    }
                }
                cinema4.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn4 = new JButton("Reset");
        resetBtn4.setFocusable(false);
        resetBtn4.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn4);
        resetBtn4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons4a.length; row++) {
                    for (int col = 0; col < seatButtons4a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus4a[row][col] = false;
                        seatButtons4a[row][col].setBackground(null);
                        seatButtons4a[row][col].setEnabled(true);
                        loadSeatStatusFromFile4a();
                        loadSeatStatusFromFile4b();
                    }
                }

                for (int row = 0; row < seatButtons4b.length; row++) {
                    for (int col = 0; col < seatButtons4b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus4b[row][col] = false;
                        seatButtons4b[row][col].setBackground(null);
                        seatButtons4b[row][col].setEnabled(true);
                        loadSeatStatusFromFile4a();
                        loadSeatStatusFromFile4b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Gomburza";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 10:00 AM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema4.add(btnPanel, BorderLayout.SOUTH);
    }
    private void createReservationButton5() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons5a.length; row++) {
                    for (int col = 0; col < seatButtons5a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus5a[row][col] = false;
                        seatButtons5a[row][col].setBackground(null);
                        seatButtons5a[row][col].setEnabled(true);
                        loadSeatStatusFromFile5a();
                        loadSeatStatusFromFile5b();
                    }
                }

                for (int row = 0; row < seatButtons5b.length; row++) {
                    for (int col = 0; col < seatButtons5b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus5b[row][col] = false;
                        seatButtons5b[row][col].setBackground(null);
                        seatButtons5b[row][col].setEnabled(true);
                        loadSeatStatusFromFile5a();
                        loadSeatStatusFromFile5b();
                    }
                }
                cinema5.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn5 = new JButton("Reset");
        resetBtn5.setFocusable(false);
        resetBtn5.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn5);
        resetBtn5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons5a.length; row++) {
                    for (int col = 0; col < seatButtons5a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus5a[row][col] = false;
                        seatButtons5a[row][col].setBackground(null);
                        seatButtons5a[row][col].setEnabled(true);
                        loadSeatStatusFromFile5a();
                        loadSeatStatusFromFile5b();
                    }
                }

                for (int row = 0; row < seatButtons5b.length; row++) {
                    for (int col = 0; col < seatButtons5b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus5b[row][col] = false;
                        seatButtons5b[row][col].setBackground(null);
                        seatButtons5b[row][col].setEnabled(true);
                        loadSeatStatusFromFile5a();
                        loadSeatStatusFromFile5b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Family Of Two";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 9:00 AM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema5.add(btnPanel, BorderLayout.SOUTH);
    }
    private void createReservationButton6() {
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton backtoMainFBtn = new JButton("Back");
        backtoMainFBtn.setFocusable(false);
        backtoMainFBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(backtoMainFBtn);
        backtoMainFBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons6a.length; row++) {
                    for (int col = 0; col < seatButtons6a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus6a[row][col] = false;
                        seatButtons6a[row][col].setBackground(null);
                        seatButtons6a[row][col].setEnabled(true);
                        loadSeatStatusFromFile6a();
                        loadSeatStatusFromFile6b();
                    }
                }

                for (int row = 0; row < seatButtons6b.length; row++) {
                    for (int col = 0; col < seatButtons6b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus6b[row][col] = false;
                        seatButtons6b[row][col].setBackground(null);
                        seatButtons6b[row][col].setEnabled(true);
                        loadSeatStatusFromFile6a();
                        loadSeatStatusFromFile6b();
                    }
                }
                cinema6.setVisible(false);
                setVisible(true);
            }
        });
        JButton resetBtn6 = new JButton("Reset");
        resetBtn6.setFocusable(false);
        resetBtn6.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(resetBtn6);
        resetBtn6.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                for (int row = 0; row < seatButtons6a.length; row++) {
                    for (int col = 0; col < seatButtons6a[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus6a[row][col] = false;
                        seatButtons6a[row][col].setBackground(null);
                        seatButtons6a[row][col].setEnabled(true);
                        loadSeatStatusFromFile6a();
                        loadSeatStatusFromFile6b();
                    }
                }

                for (int row = 0; row < seatButtons6b.length; row++) {
                    for (int col = 0; col < seatButtons6b[row].length; col++) {
                        seatRes.clear();
                        totalAmount.clear();
                        seatStatus6b[row][col] = false;
                        seatButtons6b[row][col].setBackground(null);
                        seatButtons6b[row][col].setEnabled(true);
                        loadSeatStatusFromFile6a();
                        loadSeatStatusFromFile6b();
                    }
                }
            }
        });
        JButton reserveBtn = new JButton("Reserve Seat");
        reserveBtn.setFocusable(false);
        reserveBtn.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(reserveBtn);
        reserveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(seatRes.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "Please choose a seat first!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    movie = "Penduko";
                    fillup();
                }
            }
        });
        JLabel time = new JLabel("TIME: 4:30 PM, TOMORROW");
        time.setFont(new Font("Verdana", Font.PLAIN, 14));
        btnPanel.add(time);

        cinema6.add(btnPanel, BorderLayout.SOUTH);
    }

    private void fillup(){

        name = new JTextField(5);
        name.setFont(new Font("Verdana", Font.PLAIN, 12));
        contact = new JTextField(5);
        contact.setFont(new Font("Verdana", Font.PLAIN, 12));

        JPanel panel = new JPanel(new GridLayout(5,5, 3, 2));

        JLabel nameLbl = new JLabel("Name:");
        nameLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(nameLbl);
        panel.add(name);

        JLabel contactLbl = new JLabel("Contact:");
        contactLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(contactLbl);
        panel.add(contact);

        int option = JOptionPane.showConfirmDialog(this, panel, "Fill Up", JOptionPane.OK_CANCEL_OPTION);
        if(option == JOptionPane.OK_OPTION) {
            if(name.getText().isEmpty() || contact.getText().isEmpty()) {
                JOptionPane.showMessageDialog(null, "Please out the form!", "Error", JOptionPane.ERROR_MESSAGE);
            } else {
                confirmation();
            }
        }
    }

    private void confirmation() {
        //Converting arrays into string
        StringBuilder seats = new StringBuilder("Seats Reserved: ");
        StringBuilder total = new StringBuilder();

        for(int i = 0; i < seatRes.size(); i++) {
            seats.append(seatRes.get(i));
            if(i < seatRes.size() - 1) {
                seats.append(", ");
            }
        }
        for(int i = 0; i < totalAmount.size(); i++) {
            total = new StringBuilder("Total: ₱" + totalAmount.get(i) + " ");
        }

        JPanel panel = new JPanel(new GridLayout(9,0, 3, 2));
        JLabel nameLbl = new JLabel("Name: " + name.getText());
        nameLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(nameLbl);
        JLabel contactLbl = new JLabel("Contact: " + contact.getText());
        contactLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(contactLbl);
        JLabel movieLbl = new JLabel();
        movieLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(movieLbl);
        JLabel resSeatLbl = new JLabel(String.valueOf(seats));
        resSeatLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(resSeatLbl);
        JLabel timeLbl = new JLabel();
        timeLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(timeLbl);
        JLabel cinemaLbl = new JLabel();
        cinemaLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(cinemaLbl);
        if(movie.equals("Rewind")) {
            movieLbl.setText("Movie: Rewind");
            timeLbl.setText("Time: 1:00 PM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 1");
        } else if(movie.equals("Mallari")) {
            movieLbl.setText("Movie: Mallari");
            timeLbl.setText("Time: 3:00 PM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 2");
        } else if(movie.equals("Aquaman")) {
            movieLbl.setText("Movie: Aquaman And The Lost Kingdom");
            timeLbl.setText("Time: 5:00 PM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 3");
        } else if(movie.equals("Gomburza")) {
            movieLbl.setText("Movie: Gomburza");
            timeLbl.setText("Time: 10:00 AM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 4");
        } else if(movie.equals("Family Of Two")) {
            movieLbl.setText("Movie: Family Of Two");
            timeLbl.setText("Time: 9:00 AM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 5");
        } else if(movie.equals("Penduko")) {
            movieLbl.setText("Movie: Penduko");
            timeLbl.setText("Time: 4:30 PM, Tomorrow");
            cinemaLbl.setText("Cinema: Cinema 6");
        }
        JLabel totalLbl = new JLabel(String.valueOf(total) + "\n");
        totalLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(totalLbl);
        JLabel spacer = new JLabel(" ");
        panel.add(spacer);
        JLabel takessLbl = new JLabel("Please take a screenshot or picture of this form.");
        takessLbl.setFont(new Font("Verdana", Font.PLAIN, 12));
        panel.add(takessLbl);

        int option = JOptionPane.showConfirmDialog(this, panel, "Confirmation", JOptionPane.OK_CANCEL_OPTION);
        if(option == JOptionPane.OK_OPTION){
            saveReservedtoFile();
            JOptionPane.showMessageDialog(null, "Seats reserved. Thank you!");
            if(movie.equals("Rewind")) {
                saveSeatStatusToFile1a();
                saveSeatStatusToFile1b();
                loadSeatStatusFromFile1a();
                loadSeatStatusFromFile1b();
            } else if(movie.equals("Mallari")) {
                saveSeatStatusToFile2a();
                saveSeatStatusToFile2b();
                loadSeatStatusFromFile2a();
                loadSeatStatusFromFile2b();
            } else if(movie.equals("Aquaman")) {
                saveSeatStatusToFile3a();
                saveSeatStatusToFile3b();
                loadSeatStatusFromFile3a();
                loadSeatStatusFromFile3b();
            } else if(movie.equals("Gomburza")) {
                saveSeatStatusToFile4a();
                saveSeatStatusToFile4b();
                loadSeatStatusFromFile4a();
                loadSeatStatusFromFile4b();
            } else if(movie.equals("Family Of Two")) {
                saveSeatStatusToFile5a();
                saveSeatStatusToFile5b();
                loadSeatStatusFromFile5a();
                loadSeatStatusFromFile5b();
            } else if(movie.equals("Penduko")) {
                saveSeatStatusToFile6a();
                saveSeatStatusToFile6b();
                loadSeatStatusFromFile6a();
                loadSeatStatusFromFile6b();
            }

            seatRes.clear();
            totalAmount.clear();

            if(movie.equals("Rewind")) {
                cinema1.setVisible(false);
                setVisible(true);
            } else if(movie.equals("Mallari")) {
                cinema2.setVisible(false);
                setVisible(true);
            } else if(movie.equals("Aquaman")) {
                cinema3.setVisible(false);
                setVisible(true);
            } else if(movie.equals("Gomburza")) {
                cinema4.setVisible(false);
                setVisible(true);
            } else if(movie.equals("Family Of Two")) {
                cinema5.setVisible(false);
                setVisible(true);
            } else if(movie.equals("Penduko")) {
                cinema6.setVisible(false);
                setVisible(true);
            }
        }
    }

    //SAVING SEAT STATUS TO TEXT FILE
    private void saveSeatStatusToFile1a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 1 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus1a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile1b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 1 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus1b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile2a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 2 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus2a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile2b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 2 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus2b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile3a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 3 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus3a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile3b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 3 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus3b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile4a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 4 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus4a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile4b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 4 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus4b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile5a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 5 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus5a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile5b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 5 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus5b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile6a() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 6 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus6a[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void saveSeatStatusToFile6b() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 6 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                for (int col = 0; col < 5; col++) {
                    writer.write(String.valueOf(seatStatus6b[row][col]));
                    if (col < 4) {
                        writer.write(",");
                    }
                }
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //LOADING SEAT STATUS FROM TEXT FILE
    private void loadSeatStatusFromFile1a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 1 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus1a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons1a[row][col].setEnabled(!seatStatus1a[row][col]);
                    if(seatStatus1a[row][col]) {
                        seatButtons1a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile1b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 1 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus1b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons1b[row][col].setEnabled(!seatStatus1b[row][col]);
                    if(seatStatus1b[row][col]) {
                        seatButtons1b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile2a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 2 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus2a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons2a[row][col].setEnabled(!seatStatus2a[row][col]);
                    if(seatStatus2a[row][col]) {
                        seatButtons2a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile2b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 2 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus2b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons2b[row][col].setEnabled(!seatStatus2b[row][col]);
                    if(seatStatus2b[row][col]) {
                        seatButtons2b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile3a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 3 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus3a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons3a[row][col].setEnabled(!seatStatus3a[row][col]);
                    if(seatStatus3a[row][col]) {
                        seatButtons3a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile3b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 3 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus3b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons3b[row][col].setEnabled(!seatStatus3b[row][col]);
                    if(seatStatus3b[row][col]) {
                        seatButtons3b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile4a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 4 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus4a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons4a[row][col].setEnabled(!seatStatus4a[row][col]);
                    if(seatStatus4a[row][col]) {
                        seatButtons4a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile4b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 4 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus4b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons4b[row][col].setEnabled(!seatStatus4b[row][col]);
                    if(seatStatus4b[row][col]) {
                        seatButtons4b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile5a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 5 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus5a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons5a[row][col].setEnabled(!seatStatus5a[row][col]);
                    if(seatStatus5a[row][col]) {
                        seatButtons5a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile5b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 5 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus5b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons5b[row][col].setEnabled(!seatStatus5b[row][col]);
                    if(seatStatus5b[row][col]) {
                        seatButtons5b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile6a() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 6 Seat A Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus6a[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons6a[row][col].setEnabled(!seatStatus6a[row][col]);
                    if(seatStatus6a[row][col]) {
                        seatButtons6a[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void loadSeatStatusFromFile6b() {
        try (BufferedReader reader = new BufferedReader(new FileReader("Cinema 6 Seat B Status.txt"))) {
            for (int row = 0; row < 5; row++) {
                String[] status = reader.readLine().split(",");
                for (int col = 0; col < 5; col++) {
                    seatStatus6b[row][col] = Boolean.parseBoolean(status[col]);
                    seatButtons6b[row][col].setEnabled(!seatStatus6b[row][col]);
                    if(seatStatus6b[row][col]) {
                        seatButtons6b[row][col].setBackground(Color.red);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //SAVE CUSTOMER RESERVATIONS TO TXT FILE
    private void saveReservedtoFile() {
        if(movie.equals("Rewind")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 1 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Rewind" + ", " + seatRes.get(i) + ", " + "1:00 PM, Tomorrow" + ", " + "Cinema 1" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else if(movie.equals("Mallari")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 2 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Mallari" + ", " + seatRes.get(i) + ", " + "3:00 PM, Tomorrow" + ", " + "Cinema 2" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else if(movie.equals("Aquaman")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 3 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Aquaman And The Lost Kingdom" + ", " + seatRes.get(i) + ", " + "5:00 PM, Tomorrow" + ", " + "Cinema 3" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else if(movie.equals("Gomburza")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 4 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Gomburza" + ", " + seatRes.get(i) + ", " + "10:00 AM, Tomorrow" + ", " + "Cinema 4" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else if(movie.equals("Family Of Two")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 5 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Family Of Two" + ", " + seatRes.get(i) + ", " + "9:00 AM, Tomorrow" + ", " + "Cinema 5" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else if(movie.equals("Penduko")) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("Cinema 6 Reservations.txt", true))) {
                for(int i = 0; i < seatRes.size(); i++) {
                    writer.write(name.getText() + ", " + contact.getText() + ", " + "Penduko" + ", " + seatRes.get(i) + ", " + "4:30 PM, Tomorrow" + ", " + "Cinema 6" + ", " + totalAmount.get(i));
                    if(i < seatRes.size() - 1) {
                        writer.write(" | ");
                    }
                }
                writer.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    //LAUNCHER
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new CinSeatRes();
            }
        });
    }
}