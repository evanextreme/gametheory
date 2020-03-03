class Parallel(object):

    def __init__(self, *jobs):
        self.jobs = jobs
        self.processes = []

    def fork_processes(self):
        for job in self.jobs:
            proc = Process(target=job)
            self.processes.append(proc)

    def start_all(self):
        for proc in self.processes:
            proc.start()

    def join_all(self):
        for proc in self.processes:
            proc.join()
