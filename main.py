import psutil


class SuspendAndResume:
   
    def __init__(self) -> None:
        pass

    def get_pid(self, process_name):
        for process in psutil.process_iter():
            if process.name() == process_name:
                return process.pid

    def resume_process(self, application_name):
        pid = self.get_pid(application_name)
        process = psutil.Process(pid)
        process.resume()

    def suspend_process(self, application_name):
        pid = self.get_pid(application_name)
        process = psutil.Process(pid)
        process.suspend()


