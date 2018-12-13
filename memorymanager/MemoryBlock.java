public class MemoryBlock
{
    private int start, size, end;
    private Process process;

    public MemoryBlock(int start, int size, Process process)
    {
        this.start = start;
        this.size = size;
        this.end = start + size;
        this.process = process;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }

    public Process getProcess() {
        return process;
    }

    public void setProcess(Process process) {
        this.process = process;
    }

    public String toString()
    {
        return "Start: "+this.start+" End: "+this.end+" Size: "+this.size + process.toString();
    }
}