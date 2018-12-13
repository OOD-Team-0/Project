import java.util.ArrayList;

public class MemoryManager {
    private MemoryManagerAlgorithm algorithm;
    private ArrayList<MemoryBlock> waitList;
    private ArrayList<MemoryBlock> RAM;

    /**
     * Constructor for the MemoryManager class.
     * Requires a specified algorithm for managing processes properly.
     * @param algorithm
     */
    public MemoryManager(MemoryManagerAlgorithm algorithm) {
        this.algorithm = algorithm;
        waitList = new ArrayList<>();
        RAM = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            RAM.add(new MemoryBlock((i + 10), 10)); // ten blocks, size of ten
        }
    }

    /**
     * Generates a MemoryBlock based on information from a ProcessEvent
     * @param pEvent
     * @return
     */
    private MemoryBlock createMemoryBlock(ProcessEvent pEvent) {
        // returns a memory block based on process event
        return null;
    }

    /**
     * Checks if any processes can be removed from the RAM
     * @return
     */
    public MemoryEvent cleanRAM() {
        return null;
    }

    /**
     * Removes a process from RAM
     * @param removeProcessEvent
     * @return
     */
    public MemoryEvent removeProcess(ProcessEvent removeProcessEvent) {
        return null;
    }

    /**
     * Determine what to do with a given process based on this class' algorithm.
     * Return a MemoryEvent to represent what was done with the Process
     * @param memblock
     * @return
     */
    public MemoryEvent addProcess(ProcessEvent addProcessEvent) {
       // MemoryBlock memBlock = createMemoryBlock(addProcessEvent);
        MemoryEvent memEvent;

        ArrayList<MemoryBlock> algoList = algorithm.addProcess(RAM, addProcessEvent);
        // if algoList and RAM are different, update RAM
        if (!RAM.containAll(algoList)) {
            RAM = algoList;
            memEvent = new MemoryEvent(); // fill appropriate fields
        }
        else { // else, update waitList
            waitList.add(memBlock);
            memEvent = new MemoryEvent(); // fill appropriate fields
        }

        return memEvent;
    }




    //TODO: create overload methods for handling lists of processes, rather than just a single process.
}
