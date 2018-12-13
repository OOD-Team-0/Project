public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World");

        //To shut up the errors
        FIFO fifo = new FIFO();
        MemoryEvent me = new MemoryEvent();
        MemoryManager mm = new MemoryManager();
        OS os = new OS();
        Process p = new Process();
        ProcessEvent pe = new ProcessEvent();
    }
}
