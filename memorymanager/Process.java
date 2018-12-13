public class Process {
    private int pid;
    private int endTime;
    private int size;

    public Process(int pid, int endTime, int size) {
        this.pid = pid;
        this.endTime = endTime;
        this.size = size;
    }

    public int getPid() {
        return this.pid;
    }

    public int getTime() {
        return endTime;
    }

    public int getSize() {
        return size;
    }

    @Override
    public String toString() {
        return "Process{" +
                "name='" + this.pid + '\'' +
                ", time=" + this.endTime +
                ", size=" + this.size +
                '}';
    }

    public boolean equals(Process p) {
        return this.pid == p.getPid();
    }
}
