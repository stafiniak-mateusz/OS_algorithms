from Process import Process
from FCFS import FCFS
from SJF import SJF


class Algorithms:
    def main(self):
        flag = 1
        while(flag):
            x = input(
                "\n[1] Algorytmy szeregowania procesów\n[2] Placeholder\n[0] Zakoncz \n")

            if x == '1':
                pMenu = ProcessMenu()
                pMenu.menu()
            if x == '0':
                flag = 0


class ProcessMenu:
    def menu(self):

        burst_time = []
        arrival_time = []

        process_number = input("Ilosc Procesow: ")
        print("Processor Phases and Arrival Times")

        for i in range(int(process_number)):

            burst_time.append(int(input("P"+str(i)+": ")))
            arrival_time.append(int(input("T"+str(i)+": ")))

        process_list = []

        for i in range(int(process_number)):

            p = Process(arrival_time[i], burst_time[i])
            process_list.append(p)

        choice = input("Wybierz Algorytm: \
        \n[1] First Come First Served\
        \n[2] Shortest Job First")

        if int(choice) == 1:
            fcfs = FCFS(process_list)
            fcfs.main_loop()

        if int(choice) == 2:
            sjf = SJF(process_list)
            sjf.main_loop()


a = Algorithms()
a.main()
