import java.lang.reflect.Array;
import java.util.*;

public class FirstFit implements MemoryManagerAlgorithm {

    public FirstFit() {

    }
    /*
        adds a process into a memory block in RAM and returns the list
     */
    @Override
    public ArrayList<MemoryBlock> addProcess(ArrayList<MemoryBlock> RAM,Process process) {

        int size = process.getSize();
        int index = 0;
        MemoryBlock block = null;
        MemoryBlock newBlock = null;
        Iterator<MemoryBlock> it = RAM.iterator();

        while(it.hasNext()) {
            block = it.next();
            if (block.getSize() >= size) {

                newBlock = new MemoryBlock(block.getStart(), size,process);
                RAM.add(index, newBlock);

                //have to add if process size needs to take multiple blocks, i think
            }
            index++;
        }

    return RAM;

    }

    @Override
    public void removeProcess(Process p) {

    }


}
