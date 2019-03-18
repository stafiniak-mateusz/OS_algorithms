from queue import Queue
from Process import Process
class FCFS:
    def __init__(self, process_list = []):
        self.process_list = process_list
        
    def main_loop(self):
        q = Queue()
        status = False
        tmp = Process(0,0)
        for i in range(Process.total_burst_time):

            for j in range(len(self.process_list)):

                if self.process_list[j].arrival_time == i:

                    q.put(self.process_list[j])
                    print("\nProces dodany do kolejki")
            
            
            if not status and not q.empty():
                tmp = q.get()
                status = True
                print("\nProces zdjety z kolejki")

            tmp.burst_time -= 1

            print("P"+str(tmp.number)+": "+str(tmp.burst_time))

            if tmp.burst_time == 0:
                print("Czas oczekiwania: " + str(tmp.waiting_time))
                status = False

            for var in self.process_list:
                var.waiting_time += 1
        Process.proces_number = -1
        Process.total_burst_time = 0

