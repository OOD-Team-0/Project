public class Process {
    private String name;
    private int time;
    private double size;

    public Process(String name, int time, double size) {
        this.name = name;
        this.time = time;
        this.size = size;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public double getSize() {
        return size;
    }

    public void setSize(double size) {
        this.size = size;
    }

    @Override
    public String toString() {
        return "Process{" +
                "name='" + name + '\'' +
                ", time=" + time +
                ", size=" + size +
                '}';
    }

}
