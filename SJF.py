from heapq import heappush, heappop
from Process import Process
class SJF:
    def __init__(self, process_list = []):
        self.process_list = process_list

    def main_loop(self):
        heap = []
        tmp = Process(0,0)
        for i in range(Process.total_burst_time):
            
            for j in range(Process.proces_number):
                if self.process_list[j].arrival_time == i:
                    heappush(heap, self.process_list[j])
                    print("\nProces dodany do kopca")
                        
            
            tmp = heappop(heap)
            
            tmp.burst_time -= 1
            print("P"+str(tmp.number+1)+": "+str(tmp.burst_time))
            heappush(heap, tmp)

           

            if tmp.burst_time == 0:
                print("P"+str(tmp.number+1)+"Czas oczekiwania: " + str(tmp.waiting_time))
                heappop(heap)

            for var in heap:
                var.waiting_time += 1

        Process.proces_number = -1
        Process.total_burst_time = 0
            
           
