from time import sleep

class SimulationController:
    
    def __init__(self):
        self.running = False
        self.os = None
        self.view = None

    def setOS(self, os):
        self.os = os

    def setView(self, v):
        self.view = v

    def run(self):
        while(self.running):
            self.os.run()
            sleep(2)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False