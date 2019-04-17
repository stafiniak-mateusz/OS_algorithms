from heapq import heappush, heappop
from Process import Process


class SJF:
    def __init__(self, process_list=[]):
        self.process_list = process_list

    def main_loop(self):
        heap = []
        tmp = Process(0, 0)
        for i in range(Process.total_burst_time):

            for p in self.process_list:
                if p.arrival_time == i:
                    heappush(heap, p)
                    print("\nProces dodany do kopca")

            if len(heap) != 0:
                tmp = heappop(heap)

            tmp.burst_time -= 1
            print(f"P{tmp.number+1}: {tmp.burst_time}")
            heappush(heap, tmp)

            if tmp.burst_time == 0:
                print(f"P{tmp.number+1} - Czas oczekiwania: {tmp.waiting_time}")
                heappop(heap)

            for var in heap:
                var.waiting_time += 1

        Process.proces_number = -1
        Process.total_burst_time = 0
