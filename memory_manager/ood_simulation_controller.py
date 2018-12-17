class SimulationController: 
    
    def __init__(self):
        self.os = None

    def setOS(self, os):
        self.os = os
        os.run()

    def control(self):
        pass
