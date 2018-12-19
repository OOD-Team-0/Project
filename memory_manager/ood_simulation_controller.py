
class SimulationController:
    
    def __init__(self):
        self.os = None
        self.view = None

    def setOS(self, os):
        self.os = os
        os.run()

    def setView(self, v):
        self.view = v
