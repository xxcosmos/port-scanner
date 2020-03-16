from port_scan import PortScan
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
