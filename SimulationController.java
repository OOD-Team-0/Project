public class SimulationController {

    private OS operatingSystem;
    private View view;

    /**
     * Constructor for the SimulationController class.
     * Determines what View to use in order to represent process management in an O.S.
     * @param view
     */
    public SimulationController(View view) {
        this.view = view;
    }

    /**
     * NOTE:
     *      Modify parameters to include number of processes to generate???
     *      Modify parameters to include specified Scheduler???
     *
     * Set the MemoryManagerAlgorithm in the OS and begin simulation.
     * If either the MemoryManagerAlgorithm or OS is not a valid value, throw an exception.
     * @param algorithm
     * @param system
     */
    public void startSimulation(MemoryManagerAlgorithm algorithm, OS system) {
        if (algorithm == null) {
            // throw new "InvalidAlgorithmException
        }
        if (system == null) {
            // throw new "InvalidOperatingSystemException
        }
        this.operatingSystem = system;
        operatingSystem.setMemoryManagerAlgorithm(algorithm); // method not yet included in OS
        // Generate desired number of processes
        for (int i = 0; i < 100; i++) {
            operatingSystem.generateProcess(); // method not yet included in OS
            // should this include a delay (randomized?) to allow processes to actually finish?
        }

    }


}
