class Process:

    total_burst_time = 0
    proces_number = -1

    def __init__(self, a, b):
        self.arrival_time = a
        self.burst_time = b
        self.waiting_time = 0
        self.number = self.proces_number

        Process.total_burst_time+=self.burst_time
        Process.proces_number+=1

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    
