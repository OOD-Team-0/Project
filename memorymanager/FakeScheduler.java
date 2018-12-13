import java.lang.reflect.Array;
import java.util.ArrayList;

public class FakeScheduler implements Scheduler{
    private final int MIN_SIZE = 1;     //Number of indexes of the memory array it needs
    private final int MAX_SIZE = 20;
    private final int MIN_TIME = 5;     //In seconds
    private final int MAX_TIME = 20;

    private ArrayList<Process> processes = new ArrayList<>();
    private int processNumber = 1;

    public FakeScheduler() { }

    @Override
    public ArrayList<Process> getProcesses() {
        ArrayList<Process> temp = this.processes;
        this.processes = new ArrayList<Process>();
        return temp;
    }

    private void generateProcesses() {
        int p = 1 + (int)(Math.random() * (3 - 1));
        for(int i = 0; i < p; i++) {
            Process process = new Process(processNumber++, this.generateProcessTime(), this.generateProcessSize());
            this.processes.add(process);
        }
    }

    private int generateProcessSize() {
        return MIN_SIZE + (int)(Math.random() * (MAX_SIZE - MIN_SIZE));
    }

    private int generateProcessTime() {
        return MIN_TIME + (int)(Math.random() * (MAX_TIME - MIN_TIME));
    }
}


