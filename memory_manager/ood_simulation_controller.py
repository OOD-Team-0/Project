from time import sleep

class SimulationController:
    
    def __init__(self):
        """
		    Constructor for SimulationController
			
			:param  self
        """
        self.running = False
        self.os = None
        self.view = None

    def setOS(self, os):
        """
		    Set the OS to be used in simulation.
			
			:param  self
			:param  os: OS for the simulation
        """
        self.os = os

    def setView(self, v):
        """
		    Set the View to be used in simulation.
			
			:param  self
			:param  v: View for the simulation
        """
        self.view = v

    def run(self):
        """
		    If simulation is set to 'running', then run the OS.
			
			:param  self
        """
        while(self.running):
            self.os.run()
            sleep(2)

    def start(self):
        """
		    Start running the simulation.
			Sets 'running' to True.
			
			:param  self
        """
        self.running = True

    def stop(self):
        """
		    Stop running the simulation.
			Sets 'running' to False
			
			:param  self
		"""
        self.running = False