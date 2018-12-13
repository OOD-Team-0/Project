import java.util.ArrayList;

public interface MemoryManagerAlgorithm {
    public ArrayList<MemoryBlock> addProcess(ArrayList<MemoryBlock> RAM,Process process);
    public void removeProcess(Process p);
}
