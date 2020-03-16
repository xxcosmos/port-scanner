import threading
from socket import *
from queue import *
from PyQt5.QtCore import QThread, pyqtSignal

printLock = threading.Semaphore(1)
progressLock = threading.Semaphore(1)


class PortScan(QThread):
    signal = pyqtSignal(str)
    progress_signal = pyqtSignal()
    stop_signal = pyqtSignal()

    def __init__(self, host_list, port_list, scan_times, scan_timeout):
        super().__init__()
        self.queue = Queue()
        self.timeout = scan_timeout
        self.host_list = host_list
        self.threads = []

        self.flag = threading.Event()
        self.flag.set()
        self.running = threading.Event()
        self.running.set()

        for _ in range(scan_times):
            for i in port_list:
                self.queue.put(i)

    def __del__(self):
        self.wait()

    def success_handler(self, host, port):
        text = f'{host}:{port}'
        self.signal.emit(text)

    def startScan(self):
        while not self.queue.empty() and self.running.is_set():
            port = self.queue.get_nowait()
            if progressLock.acquire():
                self.progress_signal.emit()
                progressLock.release()
            for host in self.host_list:
                self.flag.wait()
                if not self.running.is_set():
                    break

                ss = socket(AF_INET, SOCK_STREAM)
                try:
                    ss.settimeout(self.timeout)
                    ss.connect((host, port))
                    if printLock.acquire():
                        self.success_handler(host, port)
                        printLock.release()
                    ss.close()
                except:
                    ss.close()

    def run(self):
        self.threads = []
        for t in range(150):
            thread1 = threading.Thread(target=self.startScan)
            self.threads.append(thread1)
            thread1.start()
        for t in self.threads:
            t.join()
        self.stop_signal.emit()

    def pause(self):
        self.flag.clear()

    def resume(self):
        self.flag.set()

    def stop(self):
        self.flag.set()
        self.running.clear()

