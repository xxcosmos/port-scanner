import sys
import threading
from socket import *
from queue import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from ui import PortScanUI


class PortScanner(PortScanUI):

    def setupUi(self, MainWindow):
        super(PortScanner, self).setupUi(MainWindow)
        self.start_button.clicked.connect(self.start_button_action)
        self.stop_button.clicked.connect(self.stop_button_action)
        self.init_value()

    def init_value(self):
        self.progressBar.setValue(0)
        self.progress_label.setText('0 %')
        self.cnt = 0
        self.start_button_state = 0
        self.timeout_num = 0.5
        self.scan_times_num = 1
        self.port_list = []
        self.host_list = []
        self.port_scanner = None

    def append_result(self, text):
        self.result.setPlainText(self.result.toPlainText() + '\n' + text)

    def callback(self, text):
        self.append_result(text)

    def complete_callback(self):
        self.start_button_state = 0
        self.start_button.setText('开始')
        self.append_result('扫描完成！')

    def progress_callback(self):
        self.cnt += 1
        percent = int((self.cnt / len(self.port_list)) * 100)
        self.progressBar.setValue(percent)
        self.progress_label.setText(f'{percent} %')

    def stop_button_action(self):
        if self.start_button_state == 0:
            return
        self.port_scanner.stop()
        self.start_button.setText('开始')
        self.start_button_state = 0
        self.append_result('扫描被中止！')

    def start_button_action(self):
        if self.start_button_state == 0:
            # 开始
            self.init_value()
            self.start_button.setText('暂停')
            self.read_data_from_ui()
            self.port_scanner = PortScan(self.host_list, self.port_list, self.scan_times_num, self.timeout_num)

            self.port_scanner.signal.connect(self.callback)
            self.port_scanner.progress_signal.connect(self.progress_callback)
            self.port_scanner.stop_signal.connect(self.complete_callback)

            self.port_scanner.start()
            self.start_button_state = 2
            self.append_result("开始扫描...")
        elif self.start_button_state == 1:
            # 继续
            self.start_button.setText('暂停')
            self.port_scanner.resume()
            self.start_button_state = 2
            self.append_result("继续扫描...")
        else:
            # 暂停
            self.start_button.setText('继续')
            self.port_scanner.pause()
            self.start_button_state = 1
            self.append_result('暂停扫描...')

    def read_data_from_ui(self):
        network_number = f'{self.network_a.text()}.{self.network_b.text()}.{self.network_c.text()}'
        host_a = int(self.host_a.text())
        host_b = int(self.host_b.text())
        port_a = int(self.port_a.text())
        port_b = int(self.port_b.text())

        for port in range(port_a, port_b + 1):
            self.port_list.append(port)

        for host in range(host_a, host_b + 1):
            self.host_list.append(f'{network_number}.{host}')

        self.scan_times_num = int(str(self.scan_times.value()))
        self.timeout_num = self.timeout.value()


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


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = PortScanner()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
