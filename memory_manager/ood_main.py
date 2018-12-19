from ood_simulation_controller import SimulationController
from ood_os import OS
from ood_view import View
from ood_memory_manager import MemoryManager
from ood_first_fit import FirstFit
from ood_fake_scheduler import FakeScheduler
from tkinter import Tk

def main():


    memorySize = 100
    sc = SimulationController()

    ff = FirstFit()
    mm = MemoryManager(memorySize)     # Controller can probably change this
    mm.setMMA(ff)
    fs = FakeScheduler()

    v = View(memorySize)

    os = OS()
    os.setMemoryManager(mm)
    os.setScheduler(fs)
    os.addObserver(v)

    sc.setOS(os)
    sc.setView(v)
    sc.start()
    sc.run()



main()