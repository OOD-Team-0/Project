from ood_simulation_controller import SimulationController
from ood_os import OS
from ood_view import View
from ood_memory_manager import MemoryManager
from ood_first_fit import FirstFit
from ood_fake_scheduler import FakeScheduler


def main():

    memorySize = 100    # Number of indexes in the main memory array
    sc = SimulationController()

    ff = FirstFit()     # Memory Management Algorithm
    mm = MemoryManager(memorySize)
    mm.setMMA(ff)
    fs = FakeScheduler()    # Scheduler
    v = View(memorySize)    # View
    os = OS()               # OS

    os.setMemoryManager(mm)
    os.setScheduler(fs)
    os.addObserver(v)

    sc.setOS(os)
    sc.setView(v)
    sc.start()
    sc.run()



main()