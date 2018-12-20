class Process:
    def __init__(self, pid, size, endTime):
        """
        Process Constructor

        :param pid: int         Process ID
        :param size: int        Number of indexes it takes
        :param endTime: int     When the process will end
        """
        print('ID: {}, Size: {}, EndTime: {}'.format(pid, size, endTime))
        self.pid = pid          # Process ID
        self.size = size        # Number of indexes it takes up
        self.endTime = endTime  # When the process ends
