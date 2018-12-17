from ood_simulation_controller import SimulationController
from ood_os import OS
from ood_view import View
from ood_memory_manager import MemoryManager
from ood_first_fit import FirstFit

def main():
    sc = SimulationController()

    mm = MemoryManager(100)     # Controller can probably change this
    mm.setMMA(FirstFit())

    os = OS()
    os.setMemoryManager(mm)
    os.setScheduler(FakeScheduler())
    os.setView(View())

    sc.setOS(os)

main()