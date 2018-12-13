public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World");

        View v = new View();

        //To shut up the errors
        FirstFit fifo = new FirstFit();
        MemoryEvent me = new MemoryEvent();
        MemoryManager mm = new MemoryManager();
        OS os = new OS();

        Process p = new Process("Process1",5,12.5);

        ProcessEvent pe = new ProcessEvent();


    }
}
