import java.util.Observable;
import java.util.Observer;

import javax.swing.*;
import java.awt.*;

public class View implements Observer {

    private JFrame main;
    private JMenuBar menubar;

    /**
     * Constructor for the View class.
     */
    public View() {

        //Make sure the look and feel is set to windows
        try
        {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
        }
        catch(Exception e){
        }
        //Initialize everything
        initComponents();

    }

    @Override
    public void update(Observable o, Object arg) {

    }

    private void initComponents() {

        //Construct the JFrame
        main = new JFrame("Memory Manager");

        //Create a Container and set the layout to BoxLayout (Top->Bottom)
        Container pane = main.getContentPane();
        pane.setLayout(new BoxLayout(pane, BoxLayout.PAGE_AXIS));

        //Go Create a Menu Bar
        createMenuBar(main);


        ImageIcon img = new ImageIcon("memorymanager/ram.png");
        main.setIconImage(img.getImage());
        main.pack();
        //Show it
        main.setVisible(true);


    }

    private void createMenuBar(JFrame main) {

        //Create a menubar and add it to Frame
        menubar = new JMenuBar();
        main.setJMenuBar(menubar);

        JMenu menu;
        JMenuItem item;

        //Create file menu
        menu = new JMenu("File");
        menubar.add(menu);

        item = new JMenuItem("Run Simulation");
        item.setMnemonic('R');
        menu.add(item);

        menu.addSeparator();

        item = new JMenuItem("Quit");
        item.setMnemonic('Q');
        menu.add(item);

        menu = new JMenu("Help");
        menubar.add(menu);

        item = new JMenuItem("About");
        item.setMnemonic('H');
        menu.add(item);
    }
}
