import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Random;

public class SchedulerFake implements Scheduler{
    private final int MIN_SIZE = 1;     //Number of indexes of the memory array it needs
    private final int MAX_SIZE = 20;
    private final int MIN_TIME = 5;     //In seconds
    private final int MAX_TIME = 20;
    private final int MAX_RUN_TIME = 100;
    private int timeCounter;
    private Random rand;

    private ArrayList<Process> processes = new ArrayList<>();
    private int processNumber = 1;

    public SchedulerFake()
    {
        timeCounter = 0;
        rand = new Random();
    }

    @Override
    public ArrayList<Process> getProcesses() {
        ArrayList<Process> temp = this.processes;
        this.processes = new ArrayList<Process>();
        return temp;
    }

    private void generateProcess() {
        Process process = new Process(processNumber++, this.generateProcessTime(), this.generateProcessSize());
        this.processes.add(process);
    }

    private int generateProcessSize() {
        return MIN_SIZE + (int)(Math.random() * (MAX_SIZE - MIN_SIZE));
    }

    private int generateProcessTime() {
        return MIN_TIME + (int)(Math.random() * (MAX_TIME - MIN_TIME));
    }

    while(timeCounter < MAX_RUN_TIME)
    {
        MIN_TIME + (int)(Math.random() * (MAX_TIME - MIN_TIME);
        if(!(rand.nextBoolean()) && processes.size() > 0))
        {
            event = generateEndEvent(processes.size());
            processes.remove(event.getProcess());
        }
        else
        {
            event = generateStartEvent();
            processes.add(event.getProcess());
        }
        try
        {
            wait(1000);
        }
        catch (Exception e){};
        timeCounter++;
    }
}


