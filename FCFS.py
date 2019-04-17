from queue import Queue
from Process import Process


class FCFS:
    def __init__(self, process_list=[]):
        self.process_list = process_list

    def main_loop(self):
        q = Queue()
        status = False
        tmp = Process(0, 0)
        for i in range(Process.total_burst_time):

            for p in self.process_list:
                if p.arrival_time == i:
                    q.put(p)
                    print("\nProces dodany do kolejki")

            if not status and not q.empty():
                tmp = q.get()
                status = True
                print("\nProces zdjety z kolejki")

            tmp.burst_time -= 1

            print(f"P{tmp.number+1}: {tmp.burst_time}")
            if tmp.burst_time == 0:
                print(f"Czas oczekiwania: {tmp.waiting_time}")
                status = False

            for var in self.process_list:
                var.waiting_time += 1
        Process.proces_number = -1
        Process.total_burst_time = 0
